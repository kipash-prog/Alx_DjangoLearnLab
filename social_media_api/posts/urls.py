from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, CommentListView, CommentDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
 
