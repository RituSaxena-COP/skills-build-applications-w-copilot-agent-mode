from rest_framework import serializers
from .models import Profile, Activity

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'created_at']
        read_only_fields = ('id', 'user', 'created_at')


class PublicProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'bio', 'created_at']
        read_only_fields = ('id', 'username', 'bio', 'created_at')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'distance_km', 'notes', 'timestamp', 'created_at']
        read_only_fields = ('user', 'created_at')
