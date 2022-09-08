from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

articles = {
    'sports': 'Sport page',
    'finance': 'Finance page',
    'politics': 'Politics page'
}


def ViewMySite(request):
    try:
        # 'https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/'
        t = loader.get_template('first_app/ViewMySite.html')
        c = {'foo': 'bar', }
        return HttpResponse(t.render(c, request), content_type='text/html')

        # t = loader.get_template('first_app/ViewMySite.html')
        # c = {'foo': 'bar'}
        # return HttpResponse(t.render(c, request), content_type='text/html')
    except:
        return HttpResponseNotFound('No page found')


def news_view(request, topic):
    if topic == 'simple_view':
        return HttpResponseRedirect(reverse('simple_view', args=[]))

    try:
        return HttpResponse(articles[topic])
    except:
        # return HttpResponseNotFound('Page is not found')
        raise Http404('404 Generic ERROR, page is not find')  # 404.html


# https://docs.djangoproject.com/en/3.2/topics/http/urls/

def num_page_view(request, num_page):
    try:
        topic_list = list(articles.keys())
        topic = topic_list[int(num_page)]
    except:
        raise Http404('404 Generic ERROR, page is not find')  # 404.html

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))


def simple_view(request):
    return render(request, 'first_app/example.html', {})
