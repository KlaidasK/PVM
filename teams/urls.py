from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("teamsearch/", views.teamsearch, name="teamsearch"),
    path("teammanage/", views.teammanage, name='teammanage'),
]