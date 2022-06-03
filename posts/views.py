from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostView(APIView):
    permission_classes = (AllowAny,)
    def get(self, requset, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)