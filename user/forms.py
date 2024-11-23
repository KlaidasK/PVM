from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User;
        fields = ['username', 'email']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
        }