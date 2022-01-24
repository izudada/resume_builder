
from django.urls import include, path
from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name = "register"),
    path('', include('django.contrib.auth.urls')),
]
