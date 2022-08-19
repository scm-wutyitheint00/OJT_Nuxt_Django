from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
from . import managers
from django.utils.translation import gettext_lazy as _
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.IntegerField(default = 1)
    create_user_id = models.IntegerField(blank=True, null=True)
    updated_user_id = models.IntegerField(blank=True, null=True)
    deleted_user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    profile = models.CharField(max_length=255)
    type = models.CharField(max_length=1, default = "1")
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    create_user_id = models.IntegerField(blank=True, null=True)
    updated_user_id = models.IntegerField(blank=True, null=True)
    deleted_user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class Token(models.Model):
    email = models.EmailField(max_length=254)
    token = models.EmailField(max_length=500)
    create_user_id = models.IntegerField(blank=True, null=True)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField()
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    birth_date = models.DateField(null=True, blank=True)
    pro = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return f"{self.email}'s custom account"
