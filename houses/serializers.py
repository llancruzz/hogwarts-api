# Import necessary modules
from rest_framework import serializers
from .models import HouseProfile


# Define a serializer for the Contact model
class HouseProfileSerializer(serializers.ModelSerializer):
    """
    House Profile Serializer.
    """
    class Meta:
        model = HouseProfile
        fields = ('id', 'house_name', 'description', 'current_points')
