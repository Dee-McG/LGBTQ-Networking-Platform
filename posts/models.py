from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
