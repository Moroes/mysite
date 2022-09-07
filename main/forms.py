from cProfile import label
from django import forms

from .models import Post
from taggit.models import Tag


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields= '__all__'
        widgets = {'autor': forms.HiddenInput(), 'slug': forms.HiddenInput()}

    # tags = forms.ModelChoiceField(queryset=Tag.objects.all())

