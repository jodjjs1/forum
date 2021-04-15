from django.urls import path
from profil import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda r: redirect('up'), name='profil'),
    path('user/<int:userid>', views.show_up, name='up'), 

]
