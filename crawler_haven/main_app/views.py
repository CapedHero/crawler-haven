from django.urls import reverse_lazy
from django.views.generic import CreateView

from main_app.forms import WebCrawlerForm
from main_app.models import WebCrawler


class WebCrawlerCreateView(CreateView):
    model = WebCrawler
    form_class = WebCrawlerForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('web_crawler_details', kwargs={'pk': self.object.pk})

