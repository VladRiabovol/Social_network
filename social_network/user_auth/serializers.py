from user.models import User
from datetime import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['email'] = user.email
        update_login = User.objects.filter(email=user.email).update(last_login=datetime.now())
        print(update_login)
        return token


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'password2')
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

