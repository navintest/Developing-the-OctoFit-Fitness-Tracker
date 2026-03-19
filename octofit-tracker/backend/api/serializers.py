from rest_framework import serializers
from .models import Profile, Activity, Team, WorkoutSuggestion
from django.contrib.auth.models import User
from bson import ObjectId

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'goals', 'created_at']

    def get_id(self, obj):
        return str(obj.id) if isinstance(obj.id, ObjectId) else obj.id

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'calories', 'date', 'notes']

    def get_id(self, obj):
        return str(obj.id) if isinstance(obj.id, ObjectId) else obj.id

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'created_at']

    def get_id(self, obj):
        return str(obj.id) if isinstance(obj.id, ObjectId) else obj.id

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    id = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'suggestion', 'created_at']

    def get_id(self, obj):
        return str(obj.id) if isinstance(obj.id, ObjectId) else obj.id