# Import necessary modules
from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer class
    """

    # define fields for the serializer
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        A method to get the value of the 'is_owner' field.
        Get the request object from the context.
        Return whether the current user is the owner of the profile
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        A method to get the value of the 'following_id' field.
        Get the current user from the request object.
        If the user is authenticated
        Try to get the following object between the user and the profile owner
        Return the id of the following object if it exists,
        otherwise return None.
        If the user is not authenticated, return None
        """
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "is_owner",
            "following_id",
            "posts_count",
            "followers_count",
            "following_count",
        ]
