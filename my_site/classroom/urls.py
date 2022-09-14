from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thanks', views.ThanksView.as_view(), name='thanks1'),

]
