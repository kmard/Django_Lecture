
from django.urls import path
from . import views

app_name = 'formdummy'

urlpatterns = [
    path('formDummy/', views.formDummyView,name='formDummy'),
]