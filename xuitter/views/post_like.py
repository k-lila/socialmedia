from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from ..models import Post


def post_like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("você precisa estar logado para reagir"))
        return redirect("home")
