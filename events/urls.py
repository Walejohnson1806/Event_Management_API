from django.urls import path, include

from .views import RegisterUserView
urlpatterns = [
    path('auth/', include('rest_framework.urls')),  #I Provided login & logout endpoints
    path('register/', RegisterUserView.as_view(), name='user-register'),
   # path('/api/events/')
]
