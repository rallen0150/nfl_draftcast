from django.shortcuts import render
from django.views.generic import TemplateView

from bs4 import BeautifulSoup
import requests

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super().get_context_data()
        url = "http://www.espn.com/nfl/draft/rounds"
        x = requests.get(url)
        soup = BeautifulSoup(x.text, "html.parser")
        context['draftee'] = soup.find_all(class_="draftTable__headline")
        return context
