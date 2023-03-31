from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from hogwarts_api.permissions import IsOwnerOrReadOnly


# Create your views here.
class ProfileList(APIView):
    """
    Profile List View.
    List all profiles.
    """

    def get(self, request):
        profiles = Profile.objects.all()
        # Add Serializer Profile
        serializer = ProfileSerializer(
            profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Profile Detail View.
    Retrieve and edit profile by id.
    """
    # Add class to serializer. It makes the form view more readable.
    serializer_class = ProfileSerializer
    # Add permission to allow only ownwer to edit their profile details
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
