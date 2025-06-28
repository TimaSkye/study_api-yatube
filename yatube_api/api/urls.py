from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('v1/api-token-auth/',views.obtain_auth_token),
    path('v1/posts/',...),
    path('v1/posts/<int:post_id>/',...),
    path('v1/groups/',...),
    path('v1/groups/<int:group_id>/',...),
    path('v1/posts/<int:post_id>/comments/',...),
    path('v1/posts/<int:post_id>/comments/<int:comment_id>/',...),
]