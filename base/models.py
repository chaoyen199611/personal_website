from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=500)
    pub_date=models.DateTimeField('date published')