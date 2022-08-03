from rest_framework.permissions import BasePermission


class IsAdminRole(BasePermission):
    """
    Allows access only to users which has admin role.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'administrator')


class IsDeveloperRole(BasePermission):
    """
    Allows access only to users which has developer role.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'developer')


# bot/hdgsajh
# bot/dkjsahdjhass
# bot/dasgdjg2sakdjahs
