from django.urls import path
from django.views.generic import TemplateView
from . import views

# cia itraukiam view funkcijas per view.funkcijos_pav. Galit kaip pavyzdi 
# ziuret frontend app failus.
urlpatterns = [
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name='login_user'),
]
