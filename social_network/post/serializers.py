from rest_framework import serializers
from .models import Post, Like
from user.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    body = serializers.CharField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'body', 'created_at', 'updated_at', 'likes')

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['author'])
        post = Post()
        post.author = user
        post.body = validated_data['body']
        post.save()
        return post


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.CharField()
    user = serializers.CharField()

    class Meta:
        model = Post
        fields = ('id', 'post', 'user')

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['user'])
        post = Post.objects.get(id=validated_data['post'])
        like = Like()
        like.user = user
        like.post = post
        like.save()
        return like
