from django.contrib import admin
from . import models

class Ml_models_admin(admin.ModelAdmin):
    list_display = ['name','summary','url','inputs_csv']
    
    
class category_admin(admin.ModelAdmin):
    list_display = ['name','summary']

    
    
admin.site.register(models.Ml_models, Ml_models_admin)
admin.site.register(models.category, category_admin)