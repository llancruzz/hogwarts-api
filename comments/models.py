# Importing necessary modules
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """

    # Defining the fields for the Comment model
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    # Setting the default ordering for the model to be based
    # on creation time, with newest first
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
