from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User

def profil(request):
    return HttpResponse(request.user)
