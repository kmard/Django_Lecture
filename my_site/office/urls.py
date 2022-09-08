from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = 'office'

urlpatterns = [
    path('', views.list_patients, name='list_patients'),
]
