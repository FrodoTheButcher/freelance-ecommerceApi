from rest_framework import serializers


# -- REQUEST CLASSES FOR Swagger documentation --

class UserRequestCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserRequestUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)


class ProfileRequestCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    picture = serializers.ImageField(required=False)


class ProfileRequestUpdateSerializer(serializers.Serializer):
    picture = serializers.ImageField(required=False)


class CustomTokenRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
