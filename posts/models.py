from django.db import models

from djrichtextfield.models import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=254)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostComments(models.Model):
    """Replies to posts"""
    post = models.ForeignKey(Post, related_name="post_reply", on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='post_comment_owner', on_delete=models.CASCADE)
    comment = RichTextField(max_length=2500, null=False, blank=False)

    def __str__(self):
        return f"{self.comment}"