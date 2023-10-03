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

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Разрешает запрос если метод является безопасным или если пользователь
        является автором объекта.
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
