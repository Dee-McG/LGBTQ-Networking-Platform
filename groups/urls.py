from django.urls import path
from .views import (
    GroupsView, CreateGroup, EditGroup,
    GroupDetail)


urlpatterns = [
    path('', GroupsView.as_view(), name='groups'),
    path('create/', CreateGroup.as_view(), name='create_group'),
    path('view/<slug:uuid>/', GroupDetail.as_view(), name='view_group'),
    path('edit/<slug:uuid>/', EditGroup.as_view(), name='edit_groups'),
]