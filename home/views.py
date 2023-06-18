from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Profile

class IndexView(LoginRequiredMixin, TemplateView):
    """Home Page View"""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = {
            "profile": Profile.objects.get(user=self.request.user)
        }
        return context
    
