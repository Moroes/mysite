from dataclasses import field
from rest_framework import serializers
from main.models import *


class PostSelializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description' ,'autor')