from django.urls import path
from .import views

#domain.com/first_app/simple_view
urlpatterns = [
    path('simple_view', views.ViewMySite,name='MySiteView'),
    path('sports', views.sport_view,name='SportView'),
    path('finance', views.finance_view,name='SportView'),
    path('politics', views.politics_view,name='PoliticsView')
]