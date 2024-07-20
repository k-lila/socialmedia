from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile


def unfollow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        request.user.profile.follows.remove(profile)
        request.user.profile.save()
        messages.success(request, (f"você deixou de seguir {profile.user.username}"))
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("você precisa estar logado para continuar"))
        return redirect("home")
