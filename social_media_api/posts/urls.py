from django.urls import path,include
from .views import PostCreateView, PostListView, PostDetailView, CommentListView, CommentDetailView, PostViewSet, CommentViewSet,FeedView
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    from django.urls import path,include
from .views import PostCreateView, PostListView, PostDetailView, CommentListView, CommentDetailView, PostViewSet, CommentViewSet,FeedView
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/',FeedView.as_view(),name="FeedView"),
    
     
    
]
 
    
    
]
 
