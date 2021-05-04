from userforum.forms import AddArticleForm, EditArticelForm
from .models import Articles
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
#from django.template import Template

import datetime

def main(request):
    return render(request, 'main.html', {'user': request.user})

def all_articles(request):
    articles = Articles.objects.all().order_by('-publish_time')

    return render(request, 'userforum/articles.html', {'articles': articles, 'user': request.user})

def show_article(request, article_id=1):
    article = Articles.objects.get(id=article_id)

    if request.session.get(f'is_viewed_{article_id}', False):
        print(f'прочитано {article_id}')
    else:
        article.views_count += 1
        request.session[f'is_viewed_{article_id}'] = True
        article.save()
        print(f'ток прочитал {article_id}')
    
    return render(request, 'userforum/article.html', {'article': article, 'user': request.user})

def about(request):
    return HttpResponse('about')

def add_article(request):
    if request.method == 'GET': 
        if request.user.is_authenticated:
            form = AddArticleForm()
            return render(request, 'userforum/add_article.html', {'user': request.user, 'form': form})
        else:
            return redirect('login')

    if request.method == 'POST':
        form = AddArticleForm(request.POST)

        if form.is_valid():

            new_article = Articles(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                autor=request.user,
                views_count = 0
            )
            new_article.save()

        return redirect('show_article', new_article.id)
    
def edit_article(request, articel_id):
    try:
        article = Articles.objects.get(pk=articel_id)
    except (ValueError, Articles.DoesNotExist):
        messages.error(request, '404')
        return render(request, 'error_page.html', {'user': request.user})

    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.user.id == article.autor.id:
                form = EditArticelForm(initial={'title': article.title, 'text': article.text})

                return render(request, 'userforum/edit_article.html', {'user': request.user, 'article': article, 'form': form})
        
        messages.error(request, 'вы не автор')
        return redirect('login')

    if request.method == 'POST':
        form = EditArticelForm(request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.text = form.cleaned_data['text']
            article.publish_time = datetime.datetime.now()
            article.save()
    
        return redirect('show_article', article.id)
