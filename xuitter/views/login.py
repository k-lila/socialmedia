from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("você está logado"))
            return redirect("home")
        else:
            messages.success(request, ("houve um erro, tente novamente"))
            return redirect("login")
    else:
        return render(request, "login.html", {})


def user_logout(request):
    logout(request)
    messages.success(request, ("logout"))
    return redirect("home")
