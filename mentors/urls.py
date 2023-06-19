from django.urls import path
from .views import (
    SearchMentorView, SendEmail
    )

urlpatterns = [
    path('search/', SearchMentorView.as_view(), name='mentor_search'),
    path("email/<slug:id>/", SendEmail.as_view(), name="create_email"),
]
