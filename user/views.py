from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from .models import UserProfile
from django.contrib import messages

def register_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("frontend:index")
    else:
        form = UserCreationForm()
    return render(request, "register.html", { "form": form })

def custom_admin_view(request):
    return render(request, "admin.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            
            # Check if the user is a superuser (admin)
            if user.is_superuser:  # Admin user
                return redirect('user:custom_admin')  # Redirect to custom admin page
            
            # Regular user redirect
            return redirect('frontend:index')  # Default user page
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})

def badge_manage(request):
    return render(request, "badge-manage.html")


def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("frontend:index")
        
@login_required(login_url="/user/login/")
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'edit_profile':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('user:profile')

        elif form_type == 'delete_profile':
            request.user.delete()
            return redirect('frontend:index')

        # Handle profile picture update
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            return redirect('user:profile')

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })