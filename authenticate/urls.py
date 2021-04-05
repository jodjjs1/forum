from django.shortcuts import redirect
from django.urls import path
from authenticate import views

urlpatterns = [
    path('', lambda r: redirect('login')),
    path('registr', views.registr, name='registr'),
    path('login', views.logining, name='login'),

]