from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Post


def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post:
        return render(request, "post.html", {"post": post})
    else:
        messages.success(request, ("post não encontrado"))
        return redirect("home")
