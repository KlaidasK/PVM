from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    language = models.CharField(max_length=20)
    dob = models.DateField()
    bio = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.user_profile}"