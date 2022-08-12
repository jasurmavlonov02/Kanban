from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.users.models import User, Task, Project


class UserModelSerializer(ModelSerializer):
    first_name = CharField(max_length=40, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')


class RegisterModelSerializer(ModelSerializer):
    username = CharField(max_length=50)
    password = CharField(max_length=255)

    def validated_username(self, username):
        if not username.isalpha():
            raise ValidationError('Please Enter only letters')

        if User.objects.filter(username=username):
            raise ValidationError('This username already registred')

        return username

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')



