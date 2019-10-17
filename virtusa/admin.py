from django.contrib import admin
from . import models


# class PostPictureInline(admin.TabularInline):
#     model = models.PostPicture
#     fields = ['picture',]
#
#
# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#     PostPictureInline,
#     ]

class Ml_models_admin(admin.ModelAdmin):
    list_display = ['name','summary','url','inputs_csv']



class category_admin(admin.ModelAdmin):
    list_display = ['name','summary']

class homeStack_admin(admin.ModelAdmin):
        list_display = ['name','image']


class buisnessImperative_admin(admin.ModelAdmin):
        list_display = ['name','image']






admin.site.register(models.Ml_models, Ml_models_admin)
admin.site.register(models.category, category_admin)
admin.site.register(models.homeStack, homeStack_admin)
admin.site.register(models.buisnessImperative, buisnessImperative_admin)
