from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    message = 'This page is not allowed.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
        return True


class IsAdmin(BasePermission):
    message = 'This page is not allowed.'

    def has_permission(self, request, view):
        if request.user.user_type == 'Admin' or request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    message = 'This page is not allowed.'

    def has_object_permission(self, request, view, obj):
        return obj == request.user


