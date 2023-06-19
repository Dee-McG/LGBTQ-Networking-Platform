from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from profiles.models import Profile
from posts.forms import PostForm
from posts.models import Post


class IndexView(LoginRequiredMixin, TemplateView):
    """Home Page View"""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)

        # Retrieve the friends of the current user
        friends = profile.friends.all()

        # Filter posts to include only those from friends
        posts = Post.objects.filter(Q(author__profile__in=friends) | Q(author=profile.user)).order_by('-date_added')

        context["profile"] = profile
        context["form"] = PostForm()
        context["posts"] = posts
        return context


class LandingView(TemplateView):
    """Landing View"""
    template_name = 'home/landing.html'