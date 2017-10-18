from django.urls import reverse_lazy
from django.views.generic import CreateView

from main_app.models import WebCrawler


class WebCrawlerCreateView(CreateView):
    model = WebCrawler
    fields = '__all__'
    success_url = '/admin/'
