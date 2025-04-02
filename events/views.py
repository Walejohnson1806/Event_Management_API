from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserProfileSerializer, LoginSerializer
from rest_framework import generics, permissions
from .models import Event
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import EventSerializer
from rest_framework.authtoken.models import Token

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer  # ✅ Add this line
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    # Ensure users only see/update their own profile
    def get_object(self):
        return self.request.user 




class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    # Ensure users only see/update their own profile
    def get_object(self):
        return self.request.user
