from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    """
    The request is authenticated as a post author.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or obj.author == request.user)
