from typing import Optional
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Profile, FriendRequest
from .forms import ProfileForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.http import HttpResponse

# Create your views here.


@login_required
def send_friend_request(request, username):
    """Send a friend request to another user"""
    from_user = request.user.profile
    to_user = get_object_or_404(Profile, user__username=username)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user,
        to_user=to_user)

    return redirect('profile', pk=to_user.pk)


@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        to_user=request.user.profile
        )
    friend_request.from_user.friends.add(request.user.profile)
    request.user.profile.friends.add(friend_request.from_user)
    friend_request.delete()

    # Save the profile instances
    friend_request.from_user.save()
    request.user.profile.save()

    # Add success message
    messages.success(request, 'Friend request accepted successfully.')

    # Redirect to your own profile
    return redirect('profile', pk=request.user.profile.pk)


@login_required
def deny_friend_request(request, request_id):
    friend_request = get_object_or_404(
        FriendRequest,
        id=request_id,
        to_user=request.user.profile
        )
    friend_request.delete()

    # Add a success message
    messages.success(request, 'Friend request has been removed.')

    return redirect('profile', pk=request.user.profile.pk)


@login_required
def remove_friend(request, friend_id):
    friend_profile = get_object_or_404(Profile, id=friend_id)
    user_profile = request.user.profile
    user_profile.friends.remove(friend_profile)

    # Add success message
    friend_username = friend_profile.user.username
    messages.success(
        request,
        f"You have removed {friend_username} from your friends."
        )

    return redirect('profile', pk=user_profile.pk)


class ProfileView(TemplateView):
    """User Profile View"""
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        friend_request_received = profile.received_friend_requests.all()
        friend_request_sent = (
            profile in self.request.user.profile.sent_friend_requests.all()
            )
        context = {
            'profile': profile,
            'friend_request_received': friend_request_received,
            'friend_request_sent': friend_request_sent,
            'form': ProfileForm(instance=profile)
        }
        return context

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        friend_username = request.POST.get('friend_username')
        friend_profile = Profile.objects.get(user__username=friend_username)

        # send request
        profile.send_friend_request(friend_profile.user)

        return redirect('profile', pk=profile.pk)


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""
    form_class = ProfileForm
    model = Profile
    success_url = "/"

    def get_object(self, queryset=None):
        user = User.objects.get(pk=self.kwargs['pk'])
        # get the existing object or create a new one
        obj, created = self.model.objects.get_or_create(user=user)

        return obj

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.success_url = f'/profile/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
