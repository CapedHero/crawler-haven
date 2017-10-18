import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from main_app.forms import WebCrawlerForm
from main_app.models import WebCrawler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class WebCrawlerCreateView(CreateView):
    model = WebCrawler
    form_class = WebCrawlerForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('web_crawler_details', kwargs={'pk': self.object.pk})


class WebCrawlerDetails(View):
    def get(self, request, pk):
        web_crawler = WebCrawler.objects.get(pk=pk)
        web_crawler_path = os.path.join(BASE_DIR, 'media', str(web_crawler.script))
        with open(web_crawler_path, 'r') as f:
            script_text = f.read()

        context = {
            'web_crawler': web_crawler,
            'script_text': script_text,
        }

        return render(request, 'main_app/webcrawler_details.html', context)
