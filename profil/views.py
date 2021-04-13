from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from userforum.models import Articles

def profil(request):
    print(request)
    return HttpResponse('profil')

def show_up(request, userid):
    user = User.objects.get_object_or_404(pk=userid)
    articles = Articles.objects.filter(autor=user)
    if request.user == user:
        is_me = True
    else:
        is_me = False
    return render(request, 'profil/profil.html', {'user': user, 'articles': articles, 'is_me': is_me})

