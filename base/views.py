from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Article

class HomePageView(TemplateView):
    template_name="home.html"


def index(request):
    return HttpResponse("Homepage")