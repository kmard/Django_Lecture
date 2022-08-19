from django.http import HttpResponse,HttpResponseNotFound
from django.template import loader
from django.shortcuts import render



def ViewMySite(request):
    try:
        # 'https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/'
        t = loader.get_template('first_app/ViewMySite.html')
        c = {'foo': 'bar',}
        return HttpResponse(t.render(c, request), content_type='text/html')

        # t = loader.get_template('first_app/ViewMySite.html')
        # c = {'foo': 'bar'}
        # return HttpResponse(t.render(c, request), content_type='text/html')
    except:
        return HttpResponseNotFound('No page found')

def SportView(request):
    try:
        t = loader.get_template('first_app/ViewMySite.html')
        c = {'foo': 'bar',}
        return HttpResponse(t.render(c, request), content_type='text/html')
    except:
        result =  f'No page found'
        return HttpResponseNotFound(result)
