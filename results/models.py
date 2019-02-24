from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Result(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    medium = models.CharField(max_length=200)
    compound = models.CharField(max_length=200)
    detail = models.TextField()
    outputval = models.TextField(default='rsult not calculated')
    image = models.ImageField(upload_to='images/')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE) # will be changed to not delete in update
    

    def date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
