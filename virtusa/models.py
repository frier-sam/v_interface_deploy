from django.db import models
from datetime import datetime
from django import forms



class homeStack(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True,blank=False)
    summary = models.TextField(null=False,blank=False)
    home = models.BooleanField(default=False)

    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True,blank=False)
    summary = models.TextField(null=False,blank=False)
    home = models.BooleanField(default=False)
    maincategory = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    homeCategory= models.ForeignKey(homeStack,on_delete=models.CASCADE,related_name='homeCategory')
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name






class Ml_models(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True,blank=False)
    summary = models.TextField(null=False)
    content = models.TextField(null=False)
    extras = models.TextField(null= True,blank=True)
    problem_statement = models.TextField(null= True,blank=True)
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    graphImage = models.ImageField(upload_to='images/',default='images/default.jpg')
    url = models.URLField(null=True,blank=True)
    slideUrl = models.URLField(null=True,blank=True)
    inputs_csv = models.FileField(upload_to="inputs/")
    result_key = models.CharField(max_length=50,null=True,blank=True)
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    category = models.ManyToManyField(category,default=0,related_name='category')
    locations = models.CharField(max_length=100,null=True,blank=True)
    date_time = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)




    def __str__(self):
        return self.name
