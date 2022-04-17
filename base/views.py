from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Article, Profile

class HomePageView(TemplateView):

    template_name="home.html"

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['intro']=Profile.objects.get(id=1)
        return context


def index(request):
    return HttpResponse("Homepage")