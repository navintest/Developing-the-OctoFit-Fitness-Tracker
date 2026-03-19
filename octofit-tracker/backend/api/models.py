from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    goals = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s profile"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class WorkoutSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Suggestion for {self.user.username}"
