from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add_post'),
    path('all_post', views.all_post, name='all_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),

    path('add_comment/', views.add_comment, name='add_comment'),
    path('all_comments', views.all_comments, name='all_comments'),
    path('<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]