from django.urls import path
from django.views.generic import TemplateView
from . import views

# cia itraukiam view funkcijas per view.funkcijos_pav. Galit kaip pavyzdi 
# ziuret frontend app failus.
urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path('custom-admin/', views.custom_admin_view, name='custom_admin'),
]
