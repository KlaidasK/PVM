from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')    # Ensure the path matches the actual location
