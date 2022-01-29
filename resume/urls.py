
from django.urls import path

from .views import UserProfile

urlpatterns = [
    path('resume/profile', UserProfile.as_view(), name="profile"),
]
