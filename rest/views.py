from django.shortcuts import render
from rest_framework import generics

from rest.serializers import *
from .models import *


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSelializer