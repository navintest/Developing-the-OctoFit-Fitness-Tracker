from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name='Test Team')
		self.assertEqual(str(team), 'Test Team')

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		user = User.objects.create(username='testuser')
		activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories=200)
		self.assertEqual(str(activity), f"{user.username} - Run on {activity.date}")

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		user = User.objects.create(username='testuser')
		workout = Workout.objects.create(user=user, name='Morning Workout')
		self.assertEqual(str(workout), f"Morning Workout for {user.username}")

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		user = User.objects.create(username='testuser')
		leaderboard = Leaderboard.objects.create(user=user, score=100)
		self.assertEqual(str(leaderboard), f"{user.username} - 100")
