from django.http import HttpResponse
from .models import Post
from django.http.response import JsonResponse
from .serializers import PostSerializer
from django.core import serializers
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Api index.")


def post_list(request):
    if request.method == 'GET':
        qs = Post.objects.all()
        print('qssssssssss', qs)
        qs_json = serializers.serialize('json', qs)
        print(qs_json)
        return HttpResponse(qs_json, content_type='application/json')
        # queryset = Post.objects.all()
        # serializer_class = PostSerializer
