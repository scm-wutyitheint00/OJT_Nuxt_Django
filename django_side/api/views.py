from django.http import HttpResponse
from .models import Post
from django.http.response import JsonResponse
from .serializers import PasswordTokenSerializer, UserSerializer, PostSerializer, CustomUserSerializer, CustomUserRetrieveSerializer
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
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from uuid import uuid4
from .models import ResetPasswordToken
from django.utils import timezone
import datetime
import urllib.parse
from rest_framework.response import Response
from rest_framework import status


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
    parseMail = request.GET["email"]
    queryset = User.objects.filter(email=parseMail)
    returnMsg = ''
    code = uuid4()

    if not queryset:
        returnMsg = 'fail'
    else:
        # create new token
        if ResetPasswordToken.objects.filter(email=parseMail).exists():
            t = ResetPasswordToken.objects.get(email=parseMail)
            t.token = code
            t.created_at = datetime.datetime.now(tz=timezone.utc)
            t.save()

        # update exisiting token
        else:
            token = ResetPasswordToken.objects.create(email=parseMail, token=code,
                                                      created_at=datetime.datetime.now(tz=timezone.utc))
            token.save()
        url = 'http://localhost:3000/reset-password?'
        params = {'code': code}
        message = url + urllib.parse.urlencode(params)
        send_mail(
            'Password Reset Mail',
            message,
            'ayu422261@gmail.com',
            [request.GET["email"]],
            fail_silently=False,
        )
        returnMsg = 'success'

    return HttpResponse(returnMsg)


@api_view(('Post',))
@permission_classes([AllowAny])
def send_password_reset_mail(request):
    code = request.GET['code']
    try:
        existToken = ResetPasswordToken.objects.get(token=code)
    except:
        return Response('invalid code!', status=status.HTTP_400_BAD_REQUEST)

    if existToken.token != code:
        return Response('invalid code!', status=status.HTTP_400_BAD_REQUEST)

    if timezone.now() - existToken.created_at > settings.CODE_EXPIRATION_TIME:
        return Response('token is expired!', status=status.HTTP_400_BAD_REQUEST)

    return Response()


@api_view(('Post',))
@permission_classes([AllowAny])
def reset_password(request):
    code = request.GET['code']
    newpassword = request.GET['password']
    try:
        existToken = ResetPasswordToken.objects.get(token=code)
        authUser = get_user_model()
        updateAuthUser = authUser.objects.get(email=existToken.email)
        updateAuthUser.set_password(newpassword)
        updateAuthUser.save()

        # update user account
        updateUser = User.objects.get(email=existToken.email)
        updateUser.password = newpassword
        updateUser.save()

        # delete
        existToken.delete()
        return Response('password reset success!', status=status.HTTP_200_OK)
    except:
        return Response('user not found!', status=status.HTTP_404_NOT_FOUND)

    return Response()
