import os

from django.shortcuts import render, redirect
from django.views import View

from main_app.forms import WebCrawlerForm
from main_app.models import WebCrawler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class WebCrawlerCreateView(View):
    def get(self, request):
        form = WebCrawlerForm
        return render(request, 'main_app/web_crawler_form.html', {'form': form})

    def post(self, request):
        form = WebCrawlerForm(request.POST, request.FILES)

        if form.is_valid():
            web_crawler = form.save(commit=False)
            web_crawler.user = request.user
            web_crawler.save()
            return redirect('web_crawler_details', pk=web_crawler.id)
        else:
            return render(request, 'main_app/web_crawler_form.html', {'form': form})


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
        return render(request, 'main_app/web_crawler_details.html', context)
