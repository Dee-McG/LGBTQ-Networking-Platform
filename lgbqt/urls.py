from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('/', include('home.urls')),
<<<<<<< HEAD
    path('/', include('posts.urls')),
=======
    path('', include('posts.urls'))
>>>>>>> 2194ef1b431a2277a1f99d4f902ad861546fd760
]
