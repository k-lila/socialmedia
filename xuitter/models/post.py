from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    def count_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user} " f"({self.created_at:%d-%m-%Y %H:%M}): " f"{self.body}"
