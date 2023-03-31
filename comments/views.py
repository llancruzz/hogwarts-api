from rest_framework import generics, permissions
from hogwarts_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializer import CommentSerializer, CommentDetailSerializer

# Generics views List = GET and Create = PUT


class CommentList(generics.ListCreateAPIView):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
