from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Post, PostComments
from .forms import PostForm, PostCommentForm


def all_post(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'posts/all_post.html', context)


def post_detail(request, post_id):
    """ A view to show individual post details """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content', '')
        return redirect('post_detail', post_id=post_id)

    return render(request, 'posts/post_detail.html', context)


@login_required
def add_post(request):
    """ Add  post """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            post = form.save()
            messages.success(request, 'Successfully added post!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'posts/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit post """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully updated your post!')
            return redirect('home')
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
            # Print the form errors to the console for debugging
            print(form.errors)
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing post ID {post.id}')

    template = 'posts/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(context)

    return render(request, template, context)


def delete_post(request, post_id):
    """ Delete post  """
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('home'))


class CreateComment(LoginRequiredMixin, CreateView):
    """ A view to create a comment """
    form_class = PostCommentForm
    model = PostComments
    success_message = 'Successfully created comment'

    def form_valid(self, form):
        """
        Return to user home if form is valid
        """
        form.instance.user = self.request.user
        post = Post.objects.get(pk=self.kwargs["post_id"])
        form.instance.post = post
        self.success_url = f'/'
        form.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
