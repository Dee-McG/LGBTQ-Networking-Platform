import os
from django.views.generic import View, ListView
from profiles.models import Profile
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class SearchMentorView(LoginRequiredMixin, ListView):
    """Search for a profile"""
    template_name = 'mentors/find-a-mentor.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            users = Profile.objects.filter(
                Q(mentor_expertise__icontains=query) &
                Q(mentor=True)
            )

            return users
        

class SendEmail(LoginRequiredMixin, View):
    """Create mentor email"""
    def post(self, *args, **kwargs):
        mentor = User.objects.get(id=kwargs["id"])
        send_mail(
            subject="Hi I need a mentor",
            message=f"Hi please email me at {self.request.user.email} as I need a mentor with your skills",
            from_email=os.environ.get("EMAIL_HOST_USER"),
            recipient_list=[mentor.email]
        )
        messages.success(self.request, f'Email sent to {mentor.username}')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))