from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/#templateview

class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThanksView(TemplateView):
    template_name = 'classroom/thanks_page.html'