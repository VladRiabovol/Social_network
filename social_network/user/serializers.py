from rest_framework import serializers
from .models import User
#from djoser import serializers.
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'