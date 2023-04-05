# Importing necessary modules
from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime

# Creating the serializer for the Comment model


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """

    # Creating fields for the serializer
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    # A method to return whether the current user is the owner of the comment
    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    # A method to return a human-readable version of the created_at field

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    # A method to return a human-readable version of the updated_at field
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        # Specifying the fields to be included in the serialized output
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "post",
            "created_at",
            "updated_at",
            "content",
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """

    # Setting post field as read only
    post = serializers.ReadOnlyField(source="post.id")
