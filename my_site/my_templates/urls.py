from django.urls import path
from .import views

#domain.com/first_app/simple_view
urlpatterns = [
     path('', views.example_view, name='example1'),
     path('variable', views.variable_view, name='variable'),
     path('loops', views.loops_view, name='loops'),
     path('boolean', views.Bollean_view, name='boolean'),
]