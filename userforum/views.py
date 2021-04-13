from userforum.forms import AddArticleForm
from .models import Articles
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
#from django.template import Template

# Create your views here.

def main(request):

    return render(request, 'main.html', {'user': request.user})

def all_articles(request):
    articles = Articles.objects.all()


    return render(request, 'userforum/articles.html', {'articles': articles, 'user': request.user})

def show_article(request, article_id=1):
    article = Articles.objects.get(id=article_id)

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
                autor=request.user
            )
            new_article.save()

        return redirect('show_article', new_article.id)
    


