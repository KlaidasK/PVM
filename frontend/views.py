from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')   

def teamsearch(request):
    return render(request, 'teamsearch.html')

def teammanage(request):
    return render(request, "teammanage.html")