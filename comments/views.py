from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from hogwarts_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Generics views List = GET and Create = PUT


class CommentList(generics.ListCreateAPIView):
    """
    List all comments or create a comment if logged in.
    Adds three extra fields when returning a list of Comment instances
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    CommentDetail generic view:
    Retrieve a comment, or update or delete it by id if you own it.
    Allow only owner to be able to edit or delete comments.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
