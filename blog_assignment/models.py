from django.http import HttpResponse
from django.shortcuts import render
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateTimeField()
    author = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.title}"

    # def blog_posts(self):
    #     context = {'post': Article.objects.all()}
    #     response = render(request, 'index.html', context)
    #     return HttpResponse(response)