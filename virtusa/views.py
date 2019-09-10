from django.shortcuts import render
from virtusa import models
import csv
from pptx import Presentation

# Create your views here.
# home view is for home page
def home(request):
    cats = models.homeStack.objects.filter(home=True)
    mlist = [{'name':i.name,'image':i.image,'summary':i.summary ,'id':i.id,'time':i.date_time,'cats':models.category.objects.filter(homeCategory=i.id),'inps':models.Ml_models.objects.filter(category=i.id)} for i in cats]

    return render(request,'index.html',{'models':mlist})

# services view is for services
def services(request):
    cats = models.homeStack.objects.filter(home=True)
    mlist = [{'name':i.name,'image':i.image,'summary':i.summary ,'id':i.id,'time':i.date_time,'cats':models.category.objects.filter(homeCategory=i.id),'inps':models.Ml_models.objects.filter(category=i.id)} for i in cats]
    c = request.GET.get('cat')
    if c is not None:
        cats=models.category.objects.filter(homeCategory=c)
        i = models.homeStack.objects.get(id=c)

        mcatlist =  [{'name':i.name,'summary':i.summary ,'id':i.id,'inps':models.Ml_models.objects.filter(category=i.id)} for i in cats]
        mcatlist = sorted(mcatlist, key = lambda i: i['name'])
        return render(request,'services.html',{'catList':mcatlist,'modulename': i.name,'mlist':mlist})


    k = models.Ml_models.objects.filter(active=True)
    cats = models.category.objects.filter(maincategory=True)
    mcatlist =  [{'name':i.name,'summary':i.summary ,'id':i.id} for i in cats]
    mlist = [{'name':i.name,'content':i.content,'image':i.image,'summary':i.summary} for i in k]
    return render(request,'services.html',{'models':mlist,'catList':mcatlist,'mlist':mlist})


#model view is for  individual model
def model(request):
    name = request.GET['model']
    i = models.Ml_models.objects.get(name=name)
    cats = models.homeStack.objects.filter(home=True)
    mulist = [{'name':i.name,'image':i.image,'summary':i.summary ,'id':i.id,'time':i.date_time,'cats':models.category.objects.filter(homeCategory=i.id),'inps':models.Ml_models.objects.filter(category=i.id)} for i in cats]
    inps =[]
    with open(i.inputs_csv.url.split('/',1)[1], 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            inps.append({0:row[0],1:row[1]})

    mlist = {'name':i.name,'image':i.image,'summary':i.summary,'content':i.content,'extras':i.extras,'endpoint':i.url,'inputs_csv':inps,'result':i.result_key,'slide':i.slideUrl,'time':i.date_time}

    return render(request,'indview.html',{'model':mlist,'mlist':mulist})
