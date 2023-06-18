from django.urls import path
from .views import (
    GroupsView, CreateGroup, EditGroup,
    GroupDetail, DeleteGroup, CreateGroupPost,
    CreatePostComment
)


urlpatterns = [
    path('', GroupsView.as_view(), name='groups'),
    path('create/', CreateGroup.as_view(), name='create_group'),
    path('view/<slug:pk>/', GroupDetail.as_view(), name='view_group'),
    path('edit/<slug:pk>/', EditGroup.as_view(), name='edit_group'),
    path('delete/<slug:pk>/', DeleteGroup.as_view(), name='delete_group'),
    path('create/post/<slug:id>/', CreateGroupPost.as_view(), name='create_group_post'),
    path('comment/post/<slug:id>/', CreatePostComment.as_view(), name='create_post_comment'),
]