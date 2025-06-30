from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Позволяет изменять и удалять объект только его автору.
    Остальные аутентифицированные пользователи имеют доступ только на чтение.
    """
    message = (
        "Изменение и удаление чужого "
        "контента запрещено."
    )

    def has_permission(self, request, view):
        """Доступ разрешён только аутентифицированным пользователям"""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Разрешаем безопасные методы (GET, HEAD, OPTIONS)
        всем аутентифицированным.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
