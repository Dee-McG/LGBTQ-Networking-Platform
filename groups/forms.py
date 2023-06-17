from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Group

class GroupForm (forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'image', 'bio']

        labels = {
            'group_name': 'Group Name',
            'image': 'Group Image',
            'bio': 'Group Info',
        }
