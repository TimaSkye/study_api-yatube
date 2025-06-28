from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/',views.obtain_auth_token),
    path('posts/',...),
    path('posts/<int:post_id>/',...),
    path('groups/',...),
    path('groups/<int:group_id>/',...),
    path('posts/<int:post_id>/comments/',...),
    path('posts/<int:post_id>/comments/<int:comment_id>/',...),
]