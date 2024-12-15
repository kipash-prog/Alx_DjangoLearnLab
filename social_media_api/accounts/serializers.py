from rest_framework import serializers
from .models import SocialMediaUser

class SocialMediaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaUser
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = SocialMediaUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user