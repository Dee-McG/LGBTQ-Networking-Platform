from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('posts.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', include('home.urls')),
    path('profile/', include('profiles.urls')),
    path('groups/', include('groups.urls')),
    path('mentors/', include("mentors.urls")),
]
