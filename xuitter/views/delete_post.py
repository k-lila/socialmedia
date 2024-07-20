from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Post


def delete_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if request.user.username == post.user.username:
            post.delete()
            messages.success(request, ("post deletado"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            return redirect("home")
    else:
        return redirect(request.META.get("HTTP_REFERER"))
