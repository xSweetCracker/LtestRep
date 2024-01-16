from django import forms
from .models import Post


class PostCreateViewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
