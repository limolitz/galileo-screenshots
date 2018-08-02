from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Screenshot


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ListPageView(ListView):
    model = Screenshot
    template_name = 'list.html'


class ScreenshotCreate(CreateView):
    model = Screenshot
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/screenshots/list/'
