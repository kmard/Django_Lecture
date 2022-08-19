from django.http import HttpResponse, HttpResponseNotFound, Http404
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

def news_view(request,topic):
    try:
      return HttpResponse(articles[topic])
    except:
       # return HttpResponseNotFound('Page is not found')
       raise Http404('404 Generic ERROR')  #404.html

# https://docs.djangoproject.com/en/3.2/topics/http/urls/

# def sport_view(request,topic):
#     return HttpResponse(articles[topic])

# def finance_view(request,topic):
#     return HttpResponse(articles[topic])
#
# def politics_view(request,topic):
#     return HttpResponse(articles[topic])