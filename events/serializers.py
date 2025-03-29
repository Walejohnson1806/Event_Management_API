from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from .models import Event

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class EventSerializer(serializers.ModelSerializer):
    user= serializers.ReadOnlyField(source='user.username')  #Readonly user field

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'location', 'date', 'user']
        read_only_fields = ['user']  #Ensureed 'user' is never modified by API users