from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Compagnie.models import *
# Create your views here.
def home_vol(request):
    vols=Vol.objects.all()
    return  render(request,'vol/vol.html',{'vols':vols})

def information(request,pk):
    vols = Vol.objects.get(id=pk)
    compagnies=Compagnie.objects.all()
    return render(request,'vol/information.html',{'vols':vols,
                                                  'compagnies':compagnies})

