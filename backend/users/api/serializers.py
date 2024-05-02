from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import User as UserType
from users.models import Job, Staff

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }


# Serializer for Job model
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


# Serializer for Staff model
class StaffSerializer(serializers.ModelSerializer):
    job = JobSerializer()

    class Meta:
        model = Staff
        fields = ['picture', 'username', 'first_name', 'last_name', 'email', 'job',
                  'instagram_url', 'facebook_url', 'twitter_url']
