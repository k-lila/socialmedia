from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, "profile_list.html", {"profiles": profiles})
    else:
        messages.success(request, ("Você precisa estar logado para continuar"))
        return redirect("home")
