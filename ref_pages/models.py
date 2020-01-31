from __future__ import unicode_literals
from django.db import models



class Referer(models.Model):

    class Meta():
        db_table = "ref_pages_referer"
    ref_link = models.CharField(max_length=200)
    describe_link = models.TextField()
    free_test = models.BooleanField(default=True)
    personal_proxy = models.BooleanField(default=True)
    change_proxy = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    img = models.ImageField(default='img/q12.jpg')


    def __str__(self):
        return self.describe_link
