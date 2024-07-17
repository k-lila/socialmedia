from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("profiles/", profile_list, name="profiles"),
    path("profile/<int:pk>", profile, name="profile"),
]
