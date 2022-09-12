from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.list_car, name='list_car'),
    # path('list', views.list_car, name='list_car'),
    path('delete_car', views.delete_car, name='delete_car'),
    path('add_car', views.add_car, name='add_car'),
    path('rental_review', views.rental_review, name='rental_review'),
    path('rental_review_stars', views.rental_review_stars, name='rental_review_stars'),
    path('thank_you', views.thank_you, name='thank_you'),
]
