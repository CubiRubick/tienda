from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class homeDash(TemplateView):
    template_name = 'base.html'