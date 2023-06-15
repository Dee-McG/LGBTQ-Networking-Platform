from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField


# Create your models here.
class Profile(models.Model):
    """ Profile Mode """
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, null=True, default='Unspecified')
    location = models.CharField(max_length=100, null=True, default='Unspecified')
    about = RichTextField(blank=True, null=True)
    skills = models.CharField(max_length=500, null=True, default='Unspecified')
    mentor = models.BooleanField(default=False)
    mentor_expertise = models.CharField(max_length=200, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)

        