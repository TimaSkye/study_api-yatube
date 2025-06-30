from rest_framework import serializers
from posts.models import Post, Group, Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор модели Group."""

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.
    Поле author доступно только для чтения.
    Поле group сериализуется по slug.
    """
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.
    Поля author, post и created доступны только для чтения.
    """
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post', 'created')
