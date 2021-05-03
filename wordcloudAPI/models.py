from django.db import models
from datetime import datetime

# Create your models here.
class ImageUpload(models.Model):
    title = models.CharField(max_length=120)
    uid = models.CharField(max_length=200)
    S_TYPE = (
        ('U', 'URL'),
        ('T', 'TEXT')
    )
    sourceType = models.CharField(max_length=1, choices=S_TYPE, blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    wcImageURL = models.FileField(null=True, blank=True, upload_to="")
    wcImage = models.ImageField(blank=True, null=True)
    createDate = models.DateField(default=datetime.now())
    updateDate = models.DateField(default=datetime.now())

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(ImageUpload, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    message = models.TextField()
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)

class WordCloud(models.Model):
    uid = models.CharField(max_length=100)
    S_TYPE = (
        ('U', 'URL'),
        ('T', 'TEXT')
    )
    sourceType = models.CharField(max_length=1, choices=S_TYPE, blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to=uid)
    imageURL = models.URLField(max_length=400, blank=True)


