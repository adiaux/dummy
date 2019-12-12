from django.shortcuts import render
from django.http import Http404
from django.utils import timezone
from .models import item

def itemDetail(request):
    print("DJANGO SAYS",request.method,request.path,request.user)
    return render(request,"home.html",{"objs": item.objects.filter(Arrival_Date__lte=timezone.now()).order_by('Arrival_Date')}) 

def itemDetailList(request):
    return render(request,"itemList.html",{"objs": item.objects.filter(Arrival_Date__lte=timezone.now()).order_by('Arrival_Date')})

def itemDetailCreate(request):
    template_name = 'itemDetailCreate.html'
    context = {'form': None}
    return render(request, template_name, context) 



def itemDetailRetrieve(request):
    template_name = 'itemDetailRetrieve.html'
    context = {'object_list': []}
    return render(request, template_name, context) 


def itemDetailUpdate(request):
    template_name = 'itemDetailUpdate.html'
    context = {'object_list': []}
    return render(request, template_name, context) 


def itemDetailDelete(request):
    template_name = 'itemDetailDelete.html'
    context = {'object_list': []}
    return render(request, template_name, context) 
