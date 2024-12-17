from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Team name
    description = models.TextField()  # Team description
    keyword = models.CharField(max_length=50, unique=True)  # Keyword for team identification
    looking_for = models.CharField(max_length=100, blank=True)  # What kind of person the team is looking for
    requirements = models.TextField(blank=True)  # Requirements to join the team
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set default user ID or admin user
    team_leader = models.ForeignKey(User, related_name='led_teams', on_delete=models.CASCADE, null=True)  # Team leader (creator)
    members = models.ManyToManyField(User, related_name='teams')  # Many-to-many relationship for team members

    def __str__(self):
        return self.name

    def add_member(self, user):
        """Add a new member to the team."""
        self.members.add(user)

    def remove_member(self, user):
        """Remove a member from the team."""
        self.members.remove(user)

class TeamInvite(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
        ('EXPIRED', 'Expired'),
    ]
    
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='invites')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_invites')
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invites')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))

    def __str__(self):
        return f"Invite to {self.team.name} for {self.invited_user.username} - {self.status}"
    
    def accept(self):
        """Accepts the invite and adds the user to the team members."""
        if self.status == 'PENDING':
            self.team.add_member(self.invited_user)
            self.status = 'ACCEPTED'
            self.save()

    def decline(self):
        """Declines the invite."""
        if self.status == 'PENDING':
            self.status = 'DECLINED'
            self.save()

    def is_expired(self):
        """Checks if the invite is expired."""
        return timezone.now() > self.expires_at

    @classmethod
    def send_invite(cls, team, invited_user, invited_by):
        """Sends an invite."""
        invite = cls(team=team, invited_user=invited_user, invited_by=invited_by)
        invite.status = 'PENDING'
        invite.save()
        return invite

@receiver(pre_save, sender=TeamInvite)
def check_if_expired(sender, instance, **kwargs):
    """Signal to check if the invite is expired before saving."""
    if instance.is_expired() and instance.status == 'PENDING':
        instance.status = 'EXPIRED'
