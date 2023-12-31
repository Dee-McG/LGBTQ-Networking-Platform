import uuid
from django.db import models
from django.conf import settings
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class Group(models.Model):
    """
    A model to create a group
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    group_name = models.CharField(max_length=60)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE )
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="groups/", force_format='WEBP', blank=True)
    bio = RichTextField(max_length=2500, null=True, blank=True, default="No info")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members', default="None")

    
    class Meta:
        ordering = ['group_name']

    def __str__(self):
        return self.group_name


class GroupPost(models.Model):
    """Group posts"""
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='group_post_owner', on_delete=models.CASCADE)
    post = RichTextField(max_length=2500, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="group_posts/", force_format='WEBP', blank=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return f"{self.group.group_name} - {self.post}"


class GroupComments(models.Model):
    """Replies to group posts"""
    post = models.ForeignKey(GroupPost, related_name="post_comment", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='group_comment_owner', on_delete=models.CASCADE)
    comment = RichTextField(max_length=2500, null=False, blank=False)

    def __str__(self):
        return f"{self.comment}"
