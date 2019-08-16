from django.shortcuts import render
from virtusa import models
import csv
# Create your views here.
def home(request):
    cats = models.category.objects.filter(home=True)
    mlist = [{'name':i.name,'image':i.image,'summary':i.summary ,'id':i.id} for i in cats]
    return render(request,'index.html',{'models':mlist})


def services(request):
    c = request.GET.get('cat')
    if c is not None:
        k = models.Ml_models.objects.filter(category=c)
        mlist = [{'name':i.name,'image':i.image,'summary':i.summary } for i in k]
        return render(request,'services.html',{'models':mlist})

    k = models.Ml_models.objects.all()
    mlist = [{'name':i.name,'image':i.image,'summary':i.summary } for i in k]
    return render(request,'services.html',{'models':mlist})
#
# def modelsresult(request,item_url):
#     return render(request,'models.html',{'models':mlist})
def model(request):
    name = request.GET['model']
    i = models.Ml_models.objects.get(name=name)
    inps =[]
    with open(i.inputs_csv.url.split('/',1)[1], 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            inps.append({0:row[0],1:row[1]})

    mlist = {'name':i.name,'image':i.image,'summary':i.summary,'content':i.content,'extras':i.extras,'endpoint':i.url,'inputs_csv':inps,'result':i.result_key }
    return render(request,'indview.html',{'model':mlist})
