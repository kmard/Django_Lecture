
from django.urls import path
from . import views

# app_name = 'formdummy'

urlpatterns = [
    path('form/', views.formDummyView.as_view(),name='form'),
    path('formDummy/', views.formDummy.as_view(),name='formDummy'),
    path('formScheme/', views.SchemaJsonView.as_view(),name='formScheme'),
]