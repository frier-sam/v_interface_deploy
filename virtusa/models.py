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

# class slides(models.Model):
#     name = models.CharField(max_length=50,default='slides')
#     image = models.ImageField(upload_to='images/',default='images/default.jpg')
#     slide2 = models.ImageField(upload_to='images/',default='images/default.jpg')
#     slide3 = models.ImageField(upload_to='images/',default='images/default.jpg')
#
#     def __str__(self):
#         return self.name

# class PostPicture(models.Model):
#     picture = models.ImageField(upload_to='blog/post_pics', blank=True)
#     postid =models.ForeignKey('Ml_models', on_delete=models.CASCADE)



class Ml_models(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True,blank=False)
    summary = models.TextField(null=False)
    content = models.TextField(null=False)
    extras = models.TextField(null= True,blank=True)
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    url = models.URLField(null=True,blank=True)
    inputs_csv = models.FileField(upload_to="inputs/")
    result_key = models.CharField(max_length=50,null=True,blank=True)
    slide1 = models.ImageField(upload_to='images/',default='images/default.jpg')
    slide2 = models.ImageField(upload_to='images/',default='images/default.jpg')
    slide3 = models.ImageField(upload_to='images/',default='images/default.jpg')

    # slides = models.ManyToManyField(slides,default=0)
    category = models.ManyToManyField(category,default=0)
    locations = models.CharField(max_length=100,null=True,blank=True)
    date_time = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)
    # PostPicture = None



    def __str__(self):
        return self.name
