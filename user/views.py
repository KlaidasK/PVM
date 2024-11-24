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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("frontend:index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", { "form": form })

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("frontend:index")
        
@login_required(login_url="/user/login/")
def profile_view(request):
    # Get or create the user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Initialize forms with existing data (for GET or invalid POST requests)
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'edit_profile':
            # Bind the forms with POST data
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()  # Save the user data (username, email, etc.)
                profile_form.save()  # Save the profile data (bio, profile picture)
                return redirect('user:profile')  # Redirect to the profile page after saving

        elif form_type == 'delete_profile':
            # Delete the user account
            request.user.delete()
            return redirect('frontend:index')  # Redirect to the homepage after deletion

    # Render the profile page with the forms
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


