from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from .models import Screenshot
from .forms import CreateScreenshotForm
from .tasks import take_screenshot


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


def create_screenshot(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateScreenshotForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # save screenshot object
            # https://docs.djangoproject.com/en/dev/topics/db/queries/#creating-objects
            screenshot = Screenshot(url=form.cleaned_data['url'])
            screenshot.save()
            # call screenshot function
            take_screenshot.delay(screenshot.id)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('list'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateScreenshotForm()

    return render(request, 'create.html', {'form': form})

def view_screenshot(request, pk):
    screenshot = get_object_or_404(Screenshot, pk=pk)
    return render(request, 'view.html', {'screenshot': screenshot})
