from django.http import HttpResponse
from .models import Post
from django.http.response import JsonResponse
from .serializers import UserSerializer, PostSerializer, CustomUserSerializer, CustomUserRetrieveSerializer
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework import generics, permissions
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

CustomUser = get_user_model()


class CustomUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def get_object(self):
        return self.request.user


def index(request):
    return HttpResponse("Hello, world. You're at the Api index.")

