"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #home
    path('', views.home_view, name='home'),
    # my_app
    path('my_app/', include('my_app.urls')),
    #formdummy
    path('form/',include('formdummy.urls')),

    #MySiteView
    path('first_app/',include('first_app.urls')),
    #my_templates
    path('my_templates/',include('my_templates.urls')),
    #login
    path('login/', auth_views.LoginView.as_view(),name='login'),
]
