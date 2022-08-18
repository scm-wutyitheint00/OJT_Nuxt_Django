from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet

from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path("", include(router.urls)),
    # path('posts/', views.post_list, name='posts'),
]