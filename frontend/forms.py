from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CreateScreenshotForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'urlinput'}))

    def clean_url(self):
        urldata = self.cleaned_data['url']

        # check url (no relative links, contains http(s):// etc)
        # starts with http:// or https://
        if urldata[:7] != "http://" and urldata[:8] != "https://":
            raise ValidationError(_('Invalid URL'))
        # Remember to always return the cleaned data.
        return urldata
