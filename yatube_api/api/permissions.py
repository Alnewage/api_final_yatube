"""
Данный модуль содержит пользовательские классы разрешений
для Django REST Framework.
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Позволяет пользователям выполнять определенные действия только в случае
    выполнения определённых условий.
    """

    def has_permission(self, request, view):
        """
        Разрешает запрос если метод является безопасным или если пользователь
        аутентифицирован.
        """
        return True if (
            request.method in permissions.SAFE_METHODS
        ) else request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Разрешает запрос если метод является безопасным или если пользователь
        является автором объекта.
        """
        return True if (
            request.method in permissions.SAFE_METHODS
        ) else obj.author == request.user
