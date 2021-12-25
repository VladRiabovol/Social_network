from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from .models import User
from .serializers import UserActivitySerializer


class UserActivityView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'email'
