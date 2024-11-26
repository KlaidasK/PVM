from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TeamForm  # Importing the TeamForm class from the forms file
from .models import Team  # Ensure you have the correct import for your Team model
from django.contrib.auth.decorators import login_required

# View to search for teams (empty placeholder for now)
def teamsearch(request):
 # Fetch all teams from the database
    teams = Team.objects.all()  # Get all teams
    return render(request, 'teamsearch.html', {'teams': teams})

@login_required
def teammanage(request):
    # Get teams created by the currently logged-in user
    teams = Team.objects.filter(user=request.user)  # Filter teams by the logged-in user
    return render(request, 'teammanage.html', {'teams': teams})

@login_required
def teamcreate(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            new_team = form.save(commit=False)  # Don't save the user field yet
            new_team.user = request.user  # Set the logged-in user as the team creator
            new_team.save()  # Now save the team
            messages.success(request, 'Team created successfully!')
            return redirect('teams:teammanage')  # Redirect to the teammanage page after creation
        else:
            messages.error(request, 'Error creating team. Please check the form.')
    else:
        form = TeamForm()

    return render(request, 'teamcreate.html', {'form': form})
