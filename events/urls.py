from django.urls import path, include

from .views import RegisterUserView, EventListCreateView, EventDetailView, LoginView, UserProfileView

urlpatterns = [
    # path('auth/', include('rest_framework.urls')),  #I Provided login &logout endpoints.
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]

