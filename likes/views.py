# Import necessary modules
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from hogwarts_api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer


class likeList(generics.ListCreateAPIView):
    """
    List all likes. Create a like if authenticated.
    The perform_create method associates the like with the logged in user.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like. No Update view, as users can only like or unlike a post.
    Destroy a like, i.e. unlike a post if owner of that like
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
