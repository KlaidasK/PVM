from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TeamForm  # Import the TeamForm class from the forms file
from .models import Team, TeamInvite  # Import the Team model
from django.contrib.auth.models import User
from django.db.models import Q

# View to search for teams
def teamsearch(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    teams = Team.objects.filter(
        Q(name__icontains=search_query) | Q(keyword__icontains=search_query)  # Case-insensitive search
    )
    return render(request, 'teamsearch.html', {'teams': teams, 'search_query': search_query})

# Manage the teams created by the logged-in user (team leader)
@login_required
def teammanage(request):
    teams = Team.objects.filter(user=request.user)  # Filter teams created by the logged-in user
    return render(request, 'teammanage.html', {'teams': teams})

# Create a new team
@login_required
def teamcreate(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            new_team = form.save(commit=False)  # Don't save the user field yet
            new_team.user = request.user  # Set the logged-in user as the team creator
            new_team.team_leader = request.user  # Set the creator as the team leader
            new_team.save()  # Save the team
            messages.success(request, 'Team created successfully!')
            return redirect('teams:teammanage')  # Redirect to the team manage page after creation
        else:
            messages.error(request, 'Error creating team. Please check the form.')
    else:
        form = TeamForm()

    return render(request, 'teamcreate.html', {'form': form})

@login_required
def teamdetail(request, team_id):
    # Get the team object and ensure the user is the team leader
    team = get_object_or_404(Team, id=team_id)

    # Ensure the user is either the team creator or a team member
    if request.user != team.user and request.user != team.team_leader:
        messages.error(request, "You don't have permission to access this team.")
        return redirect('teams:teammanage')

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team updated successfully!')
            return redirect('teams:teammanage')
        else:
            messages.error(request, 'Error updating team. Please check the form.')
    else:
        form = TeamForm(instance=team)

    # Handle member removal
    if 'remove_member' in request.POST:
        member_id = request.POST.get('remove_member')
        member = get_object_or_404(User, id=member_id)
        team.members.remove(member)
        messages.success(request, f'{member.username} has been removed from the team.')

    return render(request, 'teamdetail.html', {'form': form, 'team': team})

# Delete team (only accessible by the team leader)
@login_required
def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    # Ensure the current user is the team leader
    if team.team_leader != request.user:
        messages.error(request, "You do not have permission to delete this team.")
        return redirect('teams:teammanage')

    if request.method == 'POST':
        team.delete()  # Delete the team
        messages.success(request, 'Team deleted successfully!')
        return redirect('teams:teammanage')  # Redirect to the teams management page

    return render(request, 'teams/confirm_delete.html', {'team': team})  # Render confirmation page

@login_required
def add_member(request, team_id, user_id):
    team = get_object_or_404(Team, id=team_id)
    user = get_object_or_404(User, id=user_id)

    # Ensure only the team leader can add members
    if team.team_leader != request.user:
        return redirect('teams:team_view', team_id=team.id)

    team.add_member(user)  # Add the user to the team's members
    return redirect('teams:team_view', team_id=team.id)

@login_required
def remove_member(request, team_id, user_id):
    team = get_object_or_404(Team, id=team_id)
    user = get_object_or_404(User, id=user_id)

    # Ensure only the team leader can remove members
    if team.team_leader != request.user:
        return redirect('teams:team_view', team_id=team.id)

    team.remove_member(user)  # Remove the user from the team's members
    return redirect('teams:team_view', team_id=team.id)

@login_required
def join_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.add_member(request.user)
    return redirect('teams:teamdetail', team_id=team.id)

@login_required
def send_invite(request, team_id, user_id):
    team = get_object_or_404(Team, id=team_id)
    invited_user = get_object_or_404(User, id=user_id)
    TeamInvite.send_invite(team, invited_user, request.user)
    return redirect('teams:teamdetail', team_id=team.id)

def usersearch(request, team_id):
    search_query = request.GET.get('search', '')
    if search_query:
        users = User.objects.filter(user__username__icontains=search_query)
    else:
        users = User.objects.all()
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'usersearch.html', {'users': users, 'search_query': search_query, 'team': team})