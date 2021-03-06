from rest_framework import serializers
from .models import User


class UserActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'last_login']


