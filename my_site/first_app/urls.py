from django.urls import path
from .import views

#domain.com/first_app/simple_view
urlpatterns = [
    path('simple_view', views.ViewMySite,name='MySiteView'),
    path('<str:topic>/', views.news_view,name='sport finance politics'),
    # path('<topic>/', views.finance_view,name='finance'),
    # path('<topic>/', views.politics_view,name='politics')
]