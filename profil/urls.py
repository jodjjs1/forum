from django.urls import path
from profil import views

urlpatterns = [
    path('', views.profil, name='profil'),
    path('user/<int:userid>', views.show_up, name='up'), 

]
