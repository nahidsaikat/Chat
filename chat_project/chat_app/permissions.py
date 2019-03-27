from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomIsAuthenticatedOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.from_user == request.user
