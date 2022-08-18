from rest_framework import serializers
from .models import Post, User
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "description", "status", "create_user_id",
              "updated_user_id", "deleted_user_id", "created_at", "updated_at", "deleted_at")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "profile", "type", "phone", "address", "dob",
              "updated_user_id", "deleted_user_id", "created_at", "updated_at", "deleted_at")

