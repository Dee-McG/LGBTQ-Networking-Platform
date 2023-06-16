from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """form to create a profile"""
    class Meta:
        model = Profile
        fields = ['job_title', 'location', 'about', 'skills']

        labels = {
            "job_title": "Job title",
            "location": "Location",
            "about": "About",
            "skills": "Skills"
        }
