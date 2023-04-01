from rest_framework import generics, permissions
from hogwarts_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class likeList(generics.ListCreateAPIView):
    """
    List all likes. Create a like if authenticated. 
    The perform_create method associates the like with the logged in user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
