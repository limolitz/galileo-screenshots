from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CreateScreenshotForm(forms.Form):
    url = forms.URLField()

    def clean_renewal_date(self):
        url = self.cleaned_data['url']

        # TODO: check url (no relative links, contains http(s):// etc)
        # Remember to always return the cleaned data.
        return data
