from django.urls import path
from .import views

#domain.com/first_app/simple_view
urlpatterns = [
    # path('simple_view', views.ViewMySite,name='MySiteView'),
    path('<int:num_page>/', views.num_page_view),
    # path('<str:topic>/', views.news_view,name='sports finance politics'),
    path('<str:topic>/', views.news_view,name='topic-page'),
    # path('<topic>/', views.politics_view,name='politics')
]