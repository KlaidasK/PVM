from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Team name
    description = models.TextField()  # Team description
    keyword = models.CharField(max_length=50, unique=True)  # Keyword for team identification
    looking_for = models.CharField(max_length=100, blank=True)  # What kind of person the team is looking for
    requirements = models.TextField(blank=True)  # Requirements to join the team
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set default user ID or admin user

    def __str__(self):
        return self.name
