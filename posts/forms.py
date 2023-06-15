from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = [
            'date_added',
            'title',
            'content'
        ]