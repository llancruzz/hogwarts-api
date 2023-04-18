# Import necessary modules
from rest_framework import generics, permissions
from hogwarts_api.permissions import IsOwnerOrReadOnly
from .models import HouseProfile
from .serializers import HouseProfileSerializer


class HouseProfileList(generics.ListCreateAPIView):
    """
    HouseProfileList generic view:
    List all profile of hogwarts'house if logged in.
    """

    serializer_class = HouseProfileSerializer
    permission_classes[permissions.IsAuthenticatedOrReadOnly]
    queryset = HouseProfile.objects.all()


class HouseProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    HouseProfileDetail generic view:
    Retrieve a contact, or update or delete it by id if you own it.
    """
    serializer_class = HouseProfileSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = HouseProfile.objects.all()
