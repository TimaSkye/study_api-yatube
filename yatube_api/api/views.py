from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для работы с постами.
    Позволяет создавать, просматривать, изменять и удалять посты.
    Доступ только для аутентифицированных пользователей.
    Изменять/удалять можно только свои посты.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Сохраняет нового автора поста."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """
        Обновляет пост, проверяя авторство.
        Вызывает PermissionDenied при попытке изменить чужой пост.
        """
        if self.request.user != self.get_object().author:
            raise PermissionDenied("Изменение чужого контента запрещено")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Удаляет пост, проверяя авторство.
        Вызывает PermissionDenied при попытке удалить чужой пост.
        """
        if self.request.user != instance.author:
            raise PermissionDenied("Удаление чужого контента запрещено")
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для просмотра групп.
    Доступ только для аутентифицированных пользователей.
    Доступны только операции чтения.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для работы с комментариями к постам.
    Доступ только для аутентифицированных пользователей.
    Изменять/удалять можно только свои комментарии.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Возвращает комментарии, относящиеся к конкретному посту,
        используя post_pk из URL.
        """
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        """Сохраняет нового автора и привязывает комментарий к посту."""
        post_id = self.kwargs['post_pk']
        serializer.save(
            author=self.request.user,
            post_id=post_id
        )

    def perform_update(self, serializer):
        """
        Обновляет комментарий, проверяя авторство.
        Вызывает PermissionDenied при попытке изменить чужой комментарий.
        """
        if self.request.user != self.get_object().author:
            raise PermissionDenied("Изменение чужого контента запрещено")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Удаляет комментарий, проверяя авторство.
        Вызывает PermissionDenied при попытке удалить чужой комментарий.
        """
        if self.request.user != instance.author:
            raise PermissionDenied("Удаление чужого контента запрещено")
        instance.delete()
