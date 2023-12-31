from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('all/', views.all_post, name='all_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('comment/<int:post_id>/', views.CreateComment.as_view(), name='post_comment'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
