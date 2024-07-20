from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import Post
from ..forms.PostForm import PostForm


def home(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, ("seu post foi publicado!"))
                return redirect("home")
        # posts = Post.objects.all().order_by("-created_at")
        followed_profiles = request.user.profile.follows.all()
        posts = Post.objects.filter(user__profile__in=followed_profiles).order_by(
            "-created_at"
        )

        return render(request, "home.html", {"posts": posts, "form": form})
    else:
        return redirect("login")
