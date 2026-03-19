from rest_framework import viewsets
from .models import Profile, Activity, Team, WorkoutSuggestion
from .serializers import ProfileSerializer, ActivitySerializer, TeamSerializer, WorkoutSuggestionSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutSuggestion.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
