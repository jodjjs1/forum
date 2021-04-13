from authenticate.forms import UserRegData
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.db.utils import IntegrityError

def registr(request):
    if request.method == 'GET':
        form = UserRegData()
        return render(request, 'authenticate/registr.html', {'user': request.user, 'form': form})

    if request.method == 'POST':
        form = UserRegData(request.POST)

        if form.is_valid():
            username = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user_un = User.objects.get(username=username)
                
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, email=email, password=password)

                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                login(request, user)

                return redirect('all_articles')
            except IntegrityError:
                messages.error(request, 'Пользователь с таким именем уже существует')
                return redirect('registr') # TODO: удаление из поля только существующие значения
            else:
                messages.error(request, 'Пользователь уже существует')
                return redirect('registr')
        else:
            return render(request, 'authenticate/registr.html', {'user': request.user, 'form': form})

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

def logouting(request):
    logout(request)
    return redirect('all_articles')
    
