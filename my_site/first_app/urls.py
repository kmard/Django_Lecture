from django.urls import path
from .import views

#domain.com/first_app/simple_view
urlpatterns = [
    path('simple_view', views.ViewMySite,name='MySiteView'),
]