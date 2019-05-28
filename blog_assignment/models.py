from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateTimeField()
    author = models.CharField(max_length=225)

    def __str__(self):
        return f'{self.title}'

class Topic(models.Model):
    category = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topic')

    def __str__(self):
        return f'{self.category}'