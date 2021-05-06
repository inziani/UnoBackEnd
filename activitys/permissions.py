from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Custom permission to restrict object editing to the owners only"""
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for any request
        # Allows GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # return super().has_object_permission(request, view, obj)
        # Write permissions are only allowed to the owner of the Activity Category
        return obj.owner == request.user

