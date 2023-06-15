from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Profile
# Create your views here.

class ProfileView(TemplateView):
    """USer Profile View"""
    template_name = "profiles/profile.html"


    def get_context_date(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            'profile' : profile
        }

        return context
