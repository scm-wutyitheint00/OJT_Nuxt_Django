from django.http import HttpResponse
from .models import Post
from django.http.response import JsonResponse
from .serializers import UserSerializer, PostSerializer
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


def index(request):
    return HttpResponse("Hello, world. You're at the Api index.")

