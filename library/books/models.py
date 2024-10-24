from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
class Author(models.Model):
    name = models.CharField(max_length=100)    
