from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Group, GroupPost, GroupComments

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'image', 'bio']

        labels = {
            'group_name': 'Group Name',
            'image': 'Group Image',
            'bio': 'Group Info',
        }


class GroupPostForm(forms.ModelForm):
    class Meta:
        model = GroupPost
        fields = ['post', 'image']

        labels = {
            'image': 'Post Image',
            'post': 'Post',
        }


class GroupCommentForm(forms.ModelForm):
    class Meta:
        model = GroupComments
        fields = ['comment']

        labels = {
            'comment': 'Comment'
        }
