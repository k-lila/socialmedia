from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile, Post


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(user_id=pk).order_by("-created_at")
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST["follow"]
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request, "profile.html", {"profile": profile, "posts": posts})
    else:
        messages.success(request, ("Você precisa estar logado para continuar"))
        return redirect("home")
