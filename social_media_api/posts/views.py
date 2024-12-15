from .models import Post, Comment
from .serializers import PostSerializers, CommmentSerializers
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions
from rest_framework import generics, permissions, filters

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated]

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommmentSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_id'])

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommmentSerializers
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]