from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog_assignment.models import Article

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