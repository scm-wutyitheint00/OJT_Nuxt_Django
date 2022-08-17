from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.IntegerField()
    create_user_id = models.IntegerField()
    updated_user_id = models.IntegerField()
    deleted_user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

class User(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    profile = models.CharField(max_length=255)
    type = models.CharField(max_length=1)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    create_user_id = models.IntegerField()
    updated_user_id = models.IntegerField()
    deleted_user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

class Token(models.Model):
    email = models.EmailField(max_length=254)
    token = models.EmailField(max_length=500)
    create_user_id = models.IntegerField()
