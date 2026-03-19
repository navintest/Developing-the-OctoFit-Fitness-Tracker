from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Profile, Activity, Team, WorkoutSuggestion
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        WorkoutSuggestion.objects.all().delete()
        Activity.objects.all().delete()
        Profile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Marvel team
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'bio': 'Genius billionaire', 'goals': 'Save the world'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'bio': 'Friendly neighborhood', 'goals': 'Protect NYC'},
        ]
        for hero in marvel_heroes:
            user = User.objects.create_user(hero['username'], hero['email'], 'password123')
            profile = Profile.objects.create(user=user, bio=hero['bio'], goals=hero['goals'])
            Activity.objects.create(user=user, activity_type='Training', duration=60, calories=500, date=timezone.now().date(), notes='Superhero training')
            WorkoutSuggestion.objects.create(user=user, suggestion='Keep up the hero work!')
            marvel.members.add(user)

        # DC team
        dc = Team.objects.create(name='Team DC', description='DC superheroes')
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'bio': 'Dark Knight', 'goals': 'Defend Gotham'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'bio': 'Amazonian warrior', 'goals': 'Promote peace'},
        ]
        for hero in dc_heroes:
            user = User.objects.create_user(hero['username'], hero['email'], 'password123')
            profile = Profile.objects.create(user=user, bio=hero['bio'], goals=hero['goals'])
            Activity.objects.create(user=user, activity_type='Training', duration=70, calories=600, date=timezone.now().date(), notes='Superhero training')
            WorkoutSuggestion.objects.create(user=user, suggestion='Stay strong and vigilant!')
            dc.members.add(user)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with Marvel and DC superheroes.'))
