"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views as ad
from user import views as us
from booking import views as bo
from knox import views as knox_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('advisor/', ad.advilist.as_view(), name='advisor'),
    path('userregister/', us.RegisterAPI.as_view(), name='register'),
    path('userlogin/', us.LoginAPI.as_view(), name='login'),
    path('userlogout/', knox_views.LogoutView.as_view(), name='logout'),
    path('userlogoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('booking/', bo.BookingCreateAPIView.as_view(), name='booking'),

]



