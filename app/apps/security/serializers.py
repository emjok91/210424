```python
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile
```