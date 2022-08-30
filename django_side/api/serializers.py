from rest_framework import serializers, validators
from .models import Post, User
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "description", "status", "created_user_id",
              "updated_user_id", "deleted_user_id", "created_at", "updated_at", "deleted_at")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "profile", "email", "type", "phone", "address", "dob",
              "updated_user_id", "deleted_user_id", "created_at", "updated_at", "deleted_at")

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'password', 'bio', 'type', 'birth_date')


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'bio', 'gender', 'birth_date', 'id')