from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import User
from .serializers import UserActivitySerializer


class UserActivityView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'email'
