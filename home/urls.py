from django.urls import path
from home.views import IndexView, LandingView


urlpatterns = [
    path('', LandingView.as_view(), name="landing"),
    path('home/', IndexView.as_view(), name="home")
]