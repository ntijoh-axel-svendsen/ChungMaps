from rest_framework import permissions


class IsMapScannerOrReadOnly(permissions.IsAuthenticated):
    """
    Custom permission to only allow map scanners to edit blocks.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return super().has_permission(request, view) and request.user.groups.filter(name='MapScanners').exists()
