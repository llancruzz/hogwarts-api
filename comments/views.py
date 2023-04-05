# Importing necessary modules
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from hogwarts_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Generics views List = GET and Create = PUT


# Creating a generic view for listing all comments and creating new comments
class CommentList(generics.ListCreateAPIView):
    """
    List all comments or create a comment if logged in.
    Adds three extra fields when returning a list of Comment instances
    """
    # Setting the serializer class for this view
    serializer_class = CommentSerializer
    # Setting the permissions for this view to allow read access
    # to anyone and write access to authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # Setting the queryset for this view to retrieve all comments
    queryset = Comment.objects.all()
    # Setting the filter backend for this view to use DjangoFilterBackend
    filter_backends = [DjangoFilterBackend]
    # Specifying the fields to be filtered on
    filterset_fields = ['post']

    # Overriding the perform_create method to set the owner
    # of the comment to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Creating a generic view for retrieving, updating and deleting a comment
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    CommentDetail generic view:
    Retrieve a comment, or update or delete it by id if you own it.
    Allow only owner to be able to edit or delete comments.
    """
    # Setting the permissions for this view to allow read access
    # to anyone and write access only to the owner of the comment
    permission_classes = [IsOwnerOrReadOnly]
    # Setting the serializer class for this view
    serializer_class = CommentDetailSerializer
    # Setting the queryset for this view to retrieve all comments
    queryset = Comment.objects.all()
