from django.shortcuts import render
from django.http import Http404
from django.utils import timezone
from .models import item

def itemDetail(request):

    return render(request,"itemList.html",{"objs": item.objects.filter(Arrival_Date__lte=timezone.now()).order_by('Arrival_Date')}) 