from django.shortcuts import render
from django.views.generic import TemplateView

# from bs4 import BeautifulSoup
# import time
# import requests

class IndexView(TemplateView):
    template_name = 'index.html'
