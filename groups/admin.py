from django.contrib import admin
from .models import Group, GroupPost, GroupComments


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupPost)
class GroupPostAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupComments)
class GroupCommentAdmin(admin.ModelAdmin):
    pass
