from django import forms

from main_app.models import WebCrawler


class WebCrawlerForm(forms.ModelForm):
    class Meta:
        model = WebCrawler
        exclude = ('user',)
        widgets = {'description': forms.Textarea()}
