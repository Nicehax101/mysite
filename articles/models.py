from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #in add thumbnail
    #add in authur
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + ' ...'