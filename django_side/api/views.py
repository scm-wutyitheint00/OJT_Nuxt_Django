from django.http import HttpResponse
from .models import Post
from django.http.response import JsonResponse
from .serializers import UserSerializer, PostSerializer, CustomUserSerializer, CustomUserRetrieveSerializer
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets, filters
from .models import User
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework import generics, permissions
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$title']


CustomUser = get_user_model()


class CustomUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

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


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ["id", "name", "email", "type", "phone", "address", "dob",
                  "updated_user_id", "deleted_user_id", "created_at", "updated_at", "deleted_at"]


def index(request):
    return HttpResponse("Hello, world. You're at the Api index.")


def send_email(request):
    send_mail(
        'Password Reset Mail',
        'We heard that you lost your password. Please reset your password with the following link',
        'ayu422261@gmail.com',
        ['wutyitheint99@gmail.com', 'scm.wutyitheint@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("success.")
