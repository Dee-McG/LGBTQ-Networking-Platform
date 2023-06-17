from django.views.generic import (
    ListView, UpdateView, CreateView, 
    DetailView
    )
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Group
from .forms import GroupForm



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
        self.success_url = f'/groups/view/{form.uuid}/'
        return super(CreateGroup, self).form_valid(form)


class GroupDetail(DetailView):
    """Blog View"""
    template_name = 'groups/view.html'
    model = Group
    context_object_name = 'group'


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
        self.success_url = f'/groups/view/{self.kwargs["uuid"]}/'
        return super().form_valid(form)

    def test_func(self):
        """
        Test requester is profile owner else throw 403
        """
        return self.request.user == self.get_object().owner