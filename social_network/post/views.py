from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer, LikeSerializer
from .models import Post, Like
from user.models import User
from django.shortcuts import render
import datetime


class ListPostView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer


class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer


class CreateLikeView(CreateAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer


class UnlikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = User.objects.get(email=request.data['user'])
        post = Post.objects.get(id=request.data['post'])
        like = Like.objects.filter(post=post, user=user)
        if like:
            like.delete()
            return Response({'message': 'delete success'}, status=status.HTTP_200_OK)
        return Response({'message': 'delete failed'}, status=status.HTTP_400_BAD_REQUEST)


class LikesRangeDateFilter(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = request.GET
        date_from = data['date_from'].split('-')
        date_to = data['date_to'].split('-')
        aggregated_by_day = dict()
        for item in range(int(date_from[2]), int(date_to[2]) + 1):
            filtering_day = datetime.date(int(date_to[0]), int(date_to[1]), int(item))
            queryset = Like.objects.filter(created_at=filtering_day)
            aggregated_by_day[str(filtering_day)] = queryset.count()
        message = 'Like analytics:'
        return Response(aggregated_by_day)


def index(request):
    return render(request, 'index.html')


