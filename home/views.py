<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Home Page View"""
    template_name = 'home/index.html'
>>>>>>> 2194ef1b431a2277a1f99d4f902ad861546fd760
