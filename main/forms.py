from django import forms

from .models import Post
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields= '__all__'
        widgets = {'autor': forms.HiddenInput(), 'slug': forms.HiddenInput(), 
        'description': forms.TextInput(attrs={"class":"input"}), 'title': forms.TextInput(attrs={"class":"input"}), 
        'tags': forms.TextInput(attrs={"class":"input"}), 'tags': LabelWidget()}
    
    # tags = TagField(required=False, widget=LabelWidget)

    # tags = forms.ModelChoiceField(queryset=Tag.objects.all())

