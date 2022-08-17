from django.shortcuts import render
from django.views import View

class formDummyView(View):
    def get(self, request,*args, **kwargs):
        return render(request,'formdummy/form.html',{'Text':'Hello all',})

# 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/'