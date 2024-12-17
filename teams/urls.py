from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'teams'  # Add this line to declare the namespace for the app

urlpatterns = [
    path("teamsearch/", views.teamsearch, name="teamsearch"),
    path("teammanage/", views.teammanage, name='teammanage'),
    path('teamcreate/', views.teamcreate, name='create-team'),
    path('detail/<int:team_id>/', views.teamdetail, name='teamdetail'), 
    path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
    path('join_team/<int:team_id>/', views.join_team, name='join_team'),
    path('usersearch/<int:team_id>/', views.usersearch, name='usersearch'),
]