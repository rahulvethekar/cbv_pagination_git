from django.db import models

# Create your models here.
class Article(models.Model):
    aid = models.IntegerField()
    aName = models.CharField(max_length=50)
    article = models.TextField()

    