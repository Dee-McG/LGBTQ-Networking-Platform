from django import forms
from .models import Post, PostComments


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]


class PostCommentForm(forms.ModelForm):

    class Meta:
        model = PostComments
        fields = [
            'comment'
        ]