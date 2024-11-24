from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'teams'  # Add this line to declare the namespace for the app

urlpatterns = [
    path("teamsearch/", views.teamsearch, name="teamsearch"),
    path("teammanage/", views.teammanage, name='teammanage'),
    path('teamcreate/', views.teamcreate, name='create-team'),
]