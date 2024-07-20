from django.shortcuts import render
from ..models import Post


def search(request):
    if request.method == "POST":
        search = request.POST["search"]
        searched = Post.objects.filter(body__contains=search)
        return render(request, "search.html", {"search": search, "searched": searched})
    else:
        return render(request, "search.html", {})
