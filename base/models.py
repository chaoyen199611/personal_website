from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class Tag(models.Model):
    icon=models.ImageField(default=' ',blank=True)
    tagname=models.CharField(max_length=50)

class Article(models.Model):
    P='P'
    A='A'
    N='N'
    I='I'
    CATEGORY=[
        (P,'Side Project'),
        (A,'Art'),
        (N,'Note'),
        (I,'Idea'),
    ]
    category = models.CharField(default=P,max_length=1,choices=CATEGORY)
    title=models.CharField(max_length=50)
    content=models.TextField()
    tags=models.ManyToManyField(Tag)
    pub_date=models.DateTimeField('date published')

class Profile(models.Model):
    introduction=models.TextField()
