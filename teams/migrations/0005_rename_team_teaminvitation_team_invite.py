# Generated by Django 5.1.4 on 2024-12-17 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_team_members_team_team_leader_teaminvitation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teaminvitation',
            old_name='team',
            new_name='team_invite',
        ),
    ]
