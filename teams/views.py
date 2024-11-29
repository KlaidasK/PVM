from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TeamForm  # Importing the TeamForm class from the forms file
from .models import Team  # Ensure you have the correct import for your Team model
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# View to search for teams (empty placeholder for now)
# Create your views here.
def teamsearch(request):
    # Get the search query from the request
    search_query = request.GET.get('search', '')
    
    # Query the teams, filtering by name if a search query is provided
    teams = Team.objects.all()
    
    teams = teams.filter(
            Q(name__icontains=search_query) | Q(keyword__icontains=search_query)  # Case-insensitive search by name or keyword
        )

    # Pass the filtered teams to the template
    return render(request, 'teamsearch.html', {'teams': teams, 'search_query': search_query})

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
