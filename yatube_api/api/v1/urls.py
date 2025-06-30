from django.urls import path, include

from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from api.v1.views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = SimpleRouter()
v1_router.register('posts',
                   PostViewSet,
                   basename='posts'
                   )
v1_router.register('groups',
                   GroupViewSet,
                   basename='groups'
                   )
v1_router.register(r'posts/(?P<post_pk>\d+)/comments',
                   CommentViewSet,
                   basename='comments'
                   )

# Вложенные роутеры комментариев к постам.
# Всё же удобнее чем регулярные выражения, ИМХО =)
# posts_router = NestedSimpleRouter(v1_router, r'posts', lookup='post')
# posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
]
