from django.db import models

# Create your models here.
class FileData(models.Model):
    userID = models.IntegerField()
    title = models.TextField()
    body = models.TextField()