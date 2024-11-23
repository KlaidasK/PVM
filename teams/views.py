from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def teamsearch(request):
    return render(request, 'teamsearch.html')

def teammanage(request):
    return render(request, "teammanage.html")