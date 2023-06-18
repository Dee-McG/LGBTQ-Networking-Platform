from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


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
            return redirect(reverse('post_detail', args=[form.pk]))
        else:
            messages.error(request, 'Failed to add post. Please ensure the form is valid.')
    else:
        form = PostForm()
   
    template = 'posts/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_post(request, post_id):
    """ Edit  post """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.name}')

    template = 'posts/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


def delete_post(request, post_id):
    """ Delete post  """
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('posts'))

""" View functions for Commenting """


def all_comments(request):
    comments = Comment.objects.all()
    context = {
        comments: comments,
    }
    return render(request, 'posts/all_comments.html', context)


def comment_detail(request, comment_id):
    """ A view to show individual comment details """
    comment = get_object_or_404(Comments, pk=comment_id)

    context = {
        comment: comment,
    }
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content', '')
        return redirect('comment_detail', comment_id=comment_id)
    return render(request, 'posts/comment_detail.html', context)


@login_required
def add_comment(request):
    """ Add  comment"""
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = request.user
            comment = form.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('comment_detail', args=[form.pk]))
        else:
            messages.error(request, 'Failed to add comment. Please ensure the form is valid.')
    else:
        form = CommentForm()

    template = 'posts/add_comment.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_comment(request, comment_id):
    """ Edit  comment"""
    comment = get_object_or_404(Post, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your comment!')
            return redirect(reverse('comment_detail', args=[comment.id]))
        else:
            messages.error(request, 'Failed to update comment. Please ensure the form is valid.')
    else:
        form = CommentForm(instance=post)
        messages.info(request, f'You are editing {comment.name}')
    template = 'posts/edit_post.html'
    context = {
        'form': form,
        comment: comment,
    }
    return render(request, template, context)


def delete_comment(request, comment_id):
    """ Delete comment """
    comment = get_object_or_404(Post, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse(comment))


