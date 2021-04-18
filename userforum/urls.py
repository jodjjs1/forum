from django.contrib import admin
from django.urls import path
from userforum import views

urlpatterns = [
    path('', views.all_articles, name='all_articles'),
    path('add_article', views.add_article, name='add_article'),
    path('id/<int:article_id>', views.show_article, name='show_article'),
    path('edit_article/<int:articel_id>', views.edit_article, name='edit_article'),
]
