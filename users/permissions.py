from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        return request.user.is_authenticated and (
            request.user.is_employee or object == request.user
        )
