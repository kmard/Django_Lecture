
from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

# app_name = 'formdummy'

urlpatterns = [
    path('form/', views.formDummyView.as_view(),name='form'),
    path('formDummy/', views.formDummy.as_view(),name='formDummy'),
    path('formScheme/', views.SchemaJsonView.as_view(),name='formScheme'),
    # path('login/', auth_views.LoginView.as_view(),name='login'),
]