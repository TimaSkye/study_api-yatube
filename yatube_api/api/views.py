from django.shortcuts import render
from rest_framework import viewsets

from api import serializers
from posts.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class GroupsViewSet:
    pass


class CommentViewSet:
    pass