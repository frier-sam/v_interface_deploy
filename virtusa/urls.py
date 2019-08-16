from django.contrib import admin
from django.urls import path,include
import virtusa.views as vview

urlpatterns = [
    path('', vview.modelsview),
    # path('<int:item_url>',vview.modelsresult,name='modelsresult'),
]
