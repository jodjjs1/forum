from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.db.utils import IntegrityError

def registr(request):
    if request.method == 'GET':
        return render(request, 'authenticate/registr.html', {'user': request.user})

    if request.method == 'POST':
        username = request.POST['login']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_un = User.objects.get(username=username)
            
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = request.POST["fname"]
            user.last_name = request.POST['sname']
            user.save()
            login(request, user)

            return redirect('all_articles')
        except IntegrityError:
            messages.error(request, 'Пользователь с таким именем уже существует')
            return redirect('registr') # TODO: удаление из поля только существующие значения
        else:
            messages.error(request, 'Пользователь уже существует')
            return redirect('registr')

def logining(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('profil')
        return render(request, 'authenticate/login.html', {'user': request.user})

    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return redirect('login')


    
