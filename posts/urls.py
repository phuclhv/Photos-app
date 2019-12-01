from django.urls import path
from .views import (
    ListPostView,
    DetailPostView,
    CreatePostView,
    DeletePostView,
    UpdatePostView
)

urlpatterns = [
    path('', ListPostView.as_view(), name='home'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post-detail'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
]
