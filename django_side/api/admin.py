from django.contrib import admin

from .models import Post, User, Token

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Token)
