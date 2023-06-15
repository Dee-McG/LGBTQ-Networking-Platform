from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'job_title',
        'location',
        'about',
        'skills'
    )


admin.site.register(Profile, ProfileAdmin)