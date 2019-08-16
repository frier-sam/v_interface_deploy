from django.db import models
from datetime import datetime
# Create your models here.



class category(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True,blank=False)
    summary = models.TextField(null=False,blank=False)
    home = models.BooleanField(default=False)
    maincategory = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Ml_models(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True,blank=False)
    summary = models.TextField(null=False)
    content = models.TextField(null=False)
    extras = models.TextField(null= True)
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    url = models.URLField(null=True,blank=True)
    inputs_csv = models.FileField(upload_to="inputs/")
    result_key = models.CharField(max_length=50,null=True,blank=True)
    category = models.ManyToManyField(category,default=0)
    locations = models.CharField(max_length=100,null=True,blank=True)
    date_time = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.name
