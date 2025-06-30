from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from posts.models import Post, Group
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для работы с постами.
    Позволяет создавать, просматривать, изменять и удалять посты.
    Доступ только для аутентифицированных пользователей.
    Изменять/удалять можно только свои посты.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """
        Сохраняет нового автора поста.
        """
        serializer.save(author=self.request.user)


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
    permission_classes = [IsAuthorOrReadOnly]

    def get_post(self):
        """
        Получить объект поста по post_pk из URL
        или вернуть 404, если не найден.
        """
        post_id = self.kwargs.get('post_pk')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        """
        Возвращает комментарии, относящиеся к конкретному посту,
        используя related_name 'comments' для выборки.
        """
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """
        Сохраняет нового автора и привязывает комментарий к посту.
        """
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
