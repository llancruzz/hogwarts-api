# Import necessary modules
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Contact


# Define a serializer for the Contact model
class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact Model.
    """

    # Define read-only fields for the owner username,
    # profile image URL, and profile ID
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    # Define methods for getting the natural language representation
    # of the created_at and updated_at fields
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    # Define methods for getting the natural language representation
    # of the created_at and updated_at fields
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    # Define the fields to be included in the serialized
    # representation of the Contact model
    class Meta:
        model = Contact
        fields = [
            "id",
            "owner",
            "reason_contact",
            "content",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
        ]
