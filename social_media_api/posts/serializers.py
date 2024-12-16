from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class PostSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model=Post
        fields='__all__'
    
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)

class CommentSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')
    
    class Meta:  
        model=Comment
        fields='__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        validated_data['post'] = self.context.get('post')
        return super().create(validated_data)
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        
