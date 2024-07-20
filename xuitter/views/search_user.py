from django.shortcuts import render
from django.contrib.auth.models import User


def search_user(request):
    if request.method == "POST":
        search = request.POST["search"]
        searched = User.objects.filter(username__contains=search)
        return render(
            request, "search_user.html", {"search": search, "searched": searched}
        )
    else:
        return render(request, "search_user.html", {})
