from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CustomUserModelViewSet, UserRetrieveUpdateDestroyAPIView, UserFilter
from django_filters.views import FilterView
from . import views


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'customuser', CustomUserModelViewSet)
# router.register(r'^users/list_food_composition/(?P<food>\w+)$', views.list_food_composition),


urlpatterns = [
    # path('', views.index, name='index'),
    path("", include(router.urls)),
    # path('posts/', views.post_list, name='posts'),
    path('data/', UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),
    path('search/(?P<food>\w+)$', views.list_food_composition),

]