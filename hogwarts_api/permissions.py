from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Create permission to check if the user is the owner.
    Only Owner is allow to edit their profile details.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
