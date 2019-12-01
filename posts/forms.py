from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """ Form to post photos """
    class Meta:
        model = Post
        fields = ['title', 'cover', 'caption']
