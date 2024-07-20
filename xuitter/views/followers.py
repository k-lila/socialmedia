from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ..models import Profile


def followers(request, pk):
    if request.user.is_authenticated:
        profiles = Profile.objects.get(user_id=pk)
        user_profile = User.objects.get(id=pk)
        return render(
            request,
            "followers.html",
            {"profiles": profiles, "user_profile": user_profile},
        )
    else:
        return redirect("home")
