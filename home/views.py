from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Home Page View"""
    template_name = 'home/index.html'
