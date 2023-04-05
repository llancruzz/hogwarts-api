# Import necessary modules
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from hogwarts_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List all posts or create a post if logged in.
    The perform_create method associates the post with the logged in user.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__followed__owner__profile",  # users feed
        "likes__owner__profile",  # users liked posts
        "owner__profile",  # users posts
        "house",  # houses category choice
    ]
    search_fields = [
        "owner__username",
        "title",
        "house",
    ]
    ordering_fields = [
        "comments_count",
        "likes_count",
        "likes_created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count("comment", distinct=True),
        likes_count=Count("likes", distinct=True),
    ).order_by("-created_at")
