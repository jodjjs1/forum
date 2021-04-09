from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User

def profil(request):
    print(request)
    return HttpResponse('profil')

def show_up(request, userid):
    user = User.objects.get(pk=userid)
    return render(request, 'profil/profil.html', {'user': request.user})
