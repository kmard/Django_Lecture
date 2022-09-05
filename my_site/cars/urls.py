from django.urls import path
from .import views


app_name = 'cars'

urlpatterns = [
    path('', views.list_car,name='list_car'),
    path('delete_car', views.delete_car,name='delete_car'),
    path('add_car', views.add_car,name='add_car'),
]