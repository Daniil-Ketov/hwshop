from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.owner == request.user:
            return True

        return False


class IsOwnerOrPost(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True

        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.method == "POST":
            return True

        if obj.owner == request.user:
            return True

        return False


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
