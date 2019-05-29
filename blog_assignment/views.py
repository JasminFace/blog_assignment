from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from blog_assignment.models import Article, Topic, Comment

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    today = date.today()
    context = {
        'todays_date': today,
        'articles': Article.objects.filter(draft=False).order_by('-published_date')
        }

    response = render(request, 'index.html', context)
    return HttpResponse(response)

def post_details(request, id):
    article = Article.objects.get(pk=id)
    context = {
        'title': article.title,
        'article': article
        }
    response = render(request, 'article_details.html', context)
    return HttpResponse(response)

@require_http_methods(['POST'])
def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.get(id=article_id)
    name = request.POST['name']
    comment = request.POST['comment']
    Comment.objects.create(name=name, message=comment, article=article)
    return redirect('article_details', id=article.id)