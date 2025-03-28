from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10, unique=True)
    branch= models.CharField(max_length=50)
    bookname = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    booknumber = models.IntegerField()
    

    def __str__(self):
        return self.name
