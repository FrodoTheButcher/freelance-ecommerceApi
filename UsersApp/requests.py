from rest_framework import serializers
from .models import User, Profile

# -- REQUEST CLASSES FOR Swagger documentation --

class UserRequestCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserRequestUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

class RegisterRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  
        user = User.objects.create_user(**validated_data)
        return user
class ProfileRequestCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    picture = serializers.ImageField(required=False)


class ProfileRequestUpdateSerializer(serializers.Serializer):
    picture = serializers.ImageField(required=False)


class CustomTokenRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
