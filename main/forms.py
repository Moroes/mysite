from cProfile import label
from django import forms

from .models import Post, Person


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['autor', 'title', 'image', 'description']

