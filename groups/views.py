from typing import Any, Dict
from django.views.generic import (
    ListView, UpdateView, CreateView, 
    DetailView, DeleteView
    )
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Group, GroupPost, GroupComments
from .forms import GroupForm, GroupPostForm, GroupCommentForm



class GroupsView(LoginRequiredMixin, ListView):
    """ A view to return groups """
    template_name = "groups/groups.html"
    model = Group
    context_object_name = 'groups'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(GroupsView, self).get_context_data(
            object_list=Group.objects.all(), form = GroupForm(), **kwargs
        )     
        return context


class CreateGroup(LoginRequiredMixin, CreateView):
    """ A view to create a group """
    form_class = GroupForm
    model = Group
    template_name = 'groups/create.html'
    success_message = 'Successfully created group'

    def form_valid(self, form):
        """
        Return to user group if form is valid
        """
        form.instance.owner = self.request.user
        form.save()
        self.success_url = f'/groups/'
        return super(CreateGroup, self).form_valid(form)


class GroupDetail(DetailView):
    """Group View"""
    template_name = 'groups/view.html'
    model = Group
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        group = self.get_object()
        context = {
            "group": group,
            "form": GroupPostForm(),
            "comment_form": GroupCommentForm(),
            "posts": GroupPost.objects.filter(group=group),
        }
        return context

    def post(self, *args, **kwargs):
        group = self.get_object()
        if group.members.filter(id=self.request.user.id).exists():
            group.members.remove(self.request.user.id)
            messages.success(
                self.request,
                f'You left {group.group_name} group'
            )
        else:
            group.members.add(self.request.user.id)
            messages.success(
                self.request,
                f'You joined {group.group_name} group'
            )
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class EditGroup(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    A view to provide a Form to the user
    to edit a group
    """
    form_class = GroupForm
    model = Group
    template_name = 'groups/edit.html'
    success_message = 'Successfully edited group'

    def form_valid(self, form):
        """
        Return to user profile if form is valid
        """
        self.success_url = f'/groups/view/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        """
        Test requester is profile owner else throw 403
        """
        return self.request.user == self.get_object().owner


class DeleteGroup(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = Group
    success_url = '/groups/'

    def test_func(self):
        return self.request.user == self.get_object().owner


class CreateGroupPost(LoginRequiredMixin, CreateView):
    """ A view to create a group """
    form_class = GroupPostForm
    model = GroupPost
    success_message = 'Successfully created post'

    def form_valid(self, form):
        """
        Return to user group if form is valid
        """
        form.instance.user = self.request.user
        group = Group.objects.get(pk=self.kwargs["id"])
        form.instance.group = group
        self.success_url = f'/groups/view/{self.kwargs["id"]}/'
        return super(CreateGroupPost, self).form_valid(form)


class CreatePostComment(LoginRequiredMixin, CreateView):
    """ A view to create a group """
    form_class = GroupCommentForm
    model = GroupComments
    success_message = 'Successfully created post'

    def form_valid(self, form):
        """
        Return to user group if form is valid
        """
        form.instance.user = self.request.user
        post = GroupPost.objects.get(pk=self.kwargs["id"])
        form.instance.post = post
        self.success_url = f'/groups/view/{self.kwargs["id"]}/'
        form.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
