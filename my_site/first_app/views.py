from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.
def ViewMySite(request):
    # 'https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/'
    t = loader.get_template('first_app/ViewMySite.html')
    c = {'foo': 'bar',}
    return HttpResponse(t.render(c, request), content_type='text/html')

    # t = loader.get_template('first_app/ViewMySite.html')
    # c = {'foo': 'bar'}
    # return HttpResponse(t.render(c, request), content_type='text/html')

