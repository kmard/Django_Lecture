
from django.urls import path
from . import views



urlpatterns = [
    path('form/', views.formDummyView.as_view(),name='form'),
    path('add/', views.FeedbackCreateView.as_view(),name='FeedbackCreate'),
    path('formScheme/', views.SchemaJsonView.as_view(),name='formScheme'),
    # path('login/', auth_views.LoginView.as_view(),name='login'),
]