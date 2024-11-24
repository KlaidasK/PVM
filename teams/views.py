from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import TeamForm #Itraukiamas is forms failo TeamForm klase
from .models import Team  # Ensure you have the correct import for your Team model
# Create your views here.
def teamsearch(request):
    return render(request, 'teamsearch.html')

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