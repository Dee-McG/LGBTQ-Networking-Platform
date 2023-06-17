from django.urls import path
from .views import (
    ProfileView,
    send_friend_request,
    accept_friend_request,
    deny_friend_request,
    remove_friend,
    EditProfile
    )

urlpatterns = [
    path('user/<slug:pk>/', ProfileView.as_view(), name="profile"),
    path('edit/<int:pk>/', EditProfile.as_view(), name='profile_edit'),
    path(
        'send-friend-request/<str:username>/',
        send_friend_request,
        name='send_friend_request'),
    path(
        'profile/accept-friend-request/<int:request_id>/',
        accept_friend_request,
        name='accept_friend_request'),
    path(
        'deny-friend-request/<int:request_id>/',
        deny_friend_request,
        name='deny_friend_request'),
    path(
        'profile/remove-friend/<int:friend_id>/',
        remove_friend,
        name='remove_friend'),
]
