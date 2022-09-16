from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thanks/', views.ThanksView.as_view(), name='thanks1'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('new_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),

]
