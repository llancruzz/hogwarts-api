# Import necessary modules
from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        # Check if the image size is greater than 2MB
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size larger than 2MB.")
        # Check if the image width is greater than 4096px
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width larger than 4096px.")
        # Check if the image height is greater than 4096px
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height larger than 4096px.")

        return value

    # Define a method to get the 'is_owner' field value
    def get_is_owner(self, obj):
        """
        Get the current request object from the context
        Check if the current user is the owner of the post
        """
        request = self.context["request"]
        return request.user == obj.owner

    # Define a method to get the 'like_id' field value
    def get_like_id(self, obj):
        """
        Get the current request object from the context.
        Check if the user is authenticated.
        Check if the user has liked the post
        """
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    # Define a Meta class to specify the model and fields to be serialized
    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "house",
            "image",
            "like_id",
            "comments_count",
            "likes_count",
        ]
