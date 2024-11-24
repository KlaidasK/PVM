from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TeamForm #Itraukiamas is forms failo TeamForm klase
from .models import Team  # Ensure you have the correct import for your Team model
from django.db.models import Q

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

def teammanage(request):
    teams = Team.objects.all()  # Get all teams from the database
    return render(request, 'teammanage.html', {'teams': teams})

def teamcreate(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            new_team = form.save()  # Save the new team
            messages.success(request, 'Team created successfully!')
            return redirect('teams:teammanage')  # Redirect to the teammanage page after creation
        else:
            messages.error(request, 'Error creating team. Please check the form.')
    else:
        form = TeamForm()

    return render(request, 'teamcreate.html', {'form': form})