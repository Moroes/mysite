from django import forms

from .models import Post
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields= '__all__'
        widgets = {'autor': forms.HiddenInput(), 'slug': forms.HiddenInput(),
        'image': forms.FileInput(attrs={"class": "image"}), 
        'description': forms.TextInput(attrs={"class": "input description"}),
        'title': forms.TextInput(attrs={"class": "input"}), 
        'tags': forms.TextInput(attrs={"class": "input"}), 'tags': LabelWidget()}