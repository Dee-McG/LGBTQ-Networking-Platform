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
        return self.club_name
