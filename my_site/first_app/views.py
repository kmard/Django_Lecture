from django.http import HttpResponse,HttpResponseNotFound
from django.template import loader
from django.shortcuts import render

articles = {
    'sports':'Sport page',
    'finance':'Finance page',
    'politics':'Politics page'
}

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

def sport_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse(articles['finance'])

def politics_view(request):
    return HttpResponse(articles['politics'])