from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from hogwarts_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    # Add class to serializer. It makes the form view more readable.
    serializer_class = ProfileSerializer
    # Add permission to allow only ownwer to edit their profile details
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
