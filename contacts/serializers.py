from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Contact
        fields = [
            'id', 'owner', 'reason_contact', 'content',
            'profile_id', 'profile_image', 'created_at', 'updated_at',
        ]
