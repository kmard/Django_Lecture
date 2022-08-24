from django.urls import path
from .import views

#register the app namespace
#URL NAMES
app_name = 'my_templates'

urlpatterns = [
     path('', views.example_view, name='example1'),
     path('variable', views.variable_view, name='variable'),
     path('loops', views.loops_view, name='loops'),
     path('boolean', views.Bollean_view, name='boolean'),
]