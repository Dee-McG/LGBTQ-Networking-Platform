from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to create/edit a profile"""
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'pronouns',
            'job_title',
            'location',
            'about',
            'skills',
            'image',
            'mentor',
            'mentor_expertise',
            ]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "pronouns": "Pronouns",
            "job_title": "Job Title",
            "location": "Location",
            "about": "About",
            "skills": "Skills",
            "image": "Profile Picture",
            'mentor': 'Mentor',
            'mentor_expertise': "Mentor Expertise",
        }

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return super().save(commit=commit)
