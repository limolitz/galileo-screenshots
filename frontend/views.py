from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Screenshot


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class RequestPageView(TemplateView):
    template_name = 'request.html'


class ListPageView(ListView):
    model = Screenshot
    template_name = 'list.html'

