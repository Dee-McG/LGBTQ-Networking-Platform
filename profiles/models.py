from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField


# Create your models here.
class Profile(models.Model):
    """ Profile Model """
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
        )
    job_title = models.CharField(
        max_length=100,
        null=True,
        default='Unspecified'
        )
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="profiles/", force_format='WEBP', blank=True)
    location = models.CharField(
        max_length=100,
        null=True,
        default='Unspecified'
        )
    about = RichTextField(
        blank=True,
        null=True
        )
    skills = models.CharField(
        max_length=500,
        null=True,
        default='Unspecified'
        )
    mentor = models.BooleanField(
        default=False
        )
    mentor_expertise = models.CharField(
        max_length=200,
        blank=True
        )
    friends = models.ManyToManyField(
        'self',
        blank=True
        )
    sent_requests = models.ManyToManyField(
        'self',
        through='FriendRequest',
        symmetrical=False,
        related_name='received_requests',
        blank=True
    )

    def __str__(self):
        return str(self.user.username)

    def send_friend_request(self, to_user):
        """Send a friend request to another user"""
        if self != to_user:
            FriendRequest.objects.create(
                from_user=self,
                to_user=to_user
                )


class FriendRequest(models.Model):
    """Friend Request Model"""
    from_user = models.ForeignKey(
        Profile,
        related_name="sent_friend_requests",
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        Profile,
        related_name="received_friend_requests",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(
            user=instance
            )
