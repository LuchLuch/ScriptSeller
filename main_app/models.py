from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.db.models import TextField
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Phonebase(models.Model):
    phone_persone = models.CharField(max_length=30)
    reg_date = models.DateTimeField('date published')
    name_persone = models.CharField(max_length=200)

    def __str__(self):
        return self.phone_persone


class Tank(models.Model):
    diz_top = models.IntegerField(default=0)
    tank_amm = models.IntegerField(default=23)
    tank_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    crew = models.IntegerField(default=3)


class Article(models.Model):
    class Meta():
        db_table = "article"

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_like = models.IntegerField(default=0)
    article_image = models.ImageField()


class Comments(models.Model):
    class Meta():
        db_table = "comments"

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article, on_delete=models.PROTECT)


class Unique_set(models.Model):
    UserAgent = models.TextField()
    IP_user = models.CharField(max_length=50)

    def __str__(self):
        return self.IP_user

# class Post(models.Model):
#     title = models.TextField()  # type:
#     cover = models.ImageField(upload_to='images/')
#
#     def __str__(self):
#         return self.title