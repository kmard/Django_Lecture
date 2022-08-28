from django.urls import path
from .import views

app_name = 'feedback'

#domain.com/first_app/simple_view
urlpatterns = [
    path('', views.simple_view,name='example-page'),  #domain.com/first_app
    path('simple_view', views.ViewMySite,name='simple_view'),
    path('<int:num_page>/', views.num_page_view,name='num-page'),
    path('<str:topic>/', views.news_view,name='topic-page'),
]