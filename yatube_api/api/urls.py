from django.urls import path

urlpatterns = [
    path('api-token-auth/',...),
    path('posts/',...),
    path('posts/<int:post_id>/',...),
    path('groups/',...),
    path('groups/<int:group_id>/',...),
    path('posts/<int:post_id>/comments/',...),
    path('posts/<int:post_id>/comments/<int:comment_id>/',...),
]