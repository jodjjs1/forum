from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from userforum.models import Articles

def show_up(request, userid):
    user = User.objects.get(pk=userid)
    articles = Articles.objects.filter(autor=user).order_by('-publish_time')
    if request.user == user:
        is_me = True
    else:
        is_me = False
    return render(request, 'profil/profil.html', {'user': request.user, 'userp': user, 'articles': articles, 'is_me': is_me})

