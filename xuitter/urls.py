from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("profiles/", profile_list, name="profiles"),
    path("profile/<int:pk>", profile, name="profile"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register_user, name="register"),
    path("update_user/", update_user, name="update_user"),
]
