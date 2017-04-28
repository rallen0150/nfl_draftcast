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
        context['draftee'] = soup.findAll('ul', {'class': 'draftTable__row'})[0].contents
        return context

class RoundView(TemplateView):
    template_name = 'round.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = "http://www.espn.com/nfl/draft/rounds/_/round/{}".format(self.kwargs['pk'])
        x = requests.get(url)
        soup = BeautifulSoup(x.text, "html.parser")
        context['player'] = soup.findAll('ul', {'class': 'draftTable__row'})[0].contents
        return context
