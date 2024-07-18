from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from ..forms import SignUpForm


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("cadastro realizado"))
            return redirect("home")
    return render(request, "register.html", {"form": form})
