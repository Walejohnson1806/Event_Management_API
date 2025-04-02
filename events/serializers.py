from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from .models import Event
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)  
    email = serializers.CharField(max_length=255)  
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventSerializer(serializers.ModelSerializer):
    user= serializers.ReadOnlyField(source='User.username')  #Readonly userfield

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'location', 'date', 'user']
        read_only_fields = ['user']  #Ensureed 'user' is never modified by API users

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)