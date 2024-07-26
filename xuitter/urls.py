from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("profiles/", profile_list, name="profiles"),
    path("profile/<int:pk>", profile, name="profile"),
    path("profile/followers/<int:pk>", followers, name="followers"),
    path("profile/follows/<int:pk>", follows, name="follows"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register_user, name="register"),
    path("update_user/", update_user, name="update_user"),
    path("post_like/<int:pk>", post_like, name="post_like"),
    path("post/<int:pk>", post, name="post"),
    path("unfollow/<int:pk>", unfollow, name="unfollow"),
    path("follow/<int:pk>", follow, name="follow"),
    path("delete_post/<int:pk>", delete_post, name="delete_post"),
    path("search/", search, name="search"),
    path("search_user/", search_user, name="search_user"),
    path("update_server/", update, name="update"),
    path("hello/", hello_world, name="hello_world"),
]
