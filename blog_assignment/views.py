from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('/home')

def home_page(request):
    today = date.today()
    context = {'todays_date': today}

    response = render(request, 'index.html', context)
    return HttpResponse(response)