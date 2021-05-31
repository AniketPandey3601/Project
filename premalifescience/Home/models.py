from django.db import models
from datetime import date


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number=models.CharField(max_length=10)
    desc=models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Products(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=15)  
    image=models.ImageField(upload_to ='uploads',null=True)


    def __str__(self):
            return self.title


class Covid_Solutions(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content=models.TextField()
    slug=models.CharField(max_length=15)  
    image=models.ImageField(null=True)


    def __str__(self):
        return self.title
 
