from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  Compagnie
from Vol.models import *
from Vol.forms import *
from .forms import *
# Create your views here.

def home_compagnie(request):
    compagnies=Compagnie.objects.all()
    return  render(request,'compagnie/compagnie.html',{'compagnies':compagnies})

def modifier_compagnie(request,pk):
    compagnie = Compagnie.objects.get(id=pk)
    form = CompagnieForm(instance=compagnie)
    if request.method == 'POST':
        form = CompagnieForm(request.POST, request.FILES, instance=compagnie)
        if form.is_valid():
            form.save()
            return redirect('/compagnie')
        compagnie.save()
    return render(request, 'compagnie/compagnie_update.html',{'form':form,'compagnie':compagnie})

def information(request,pk):
    compagnies=Compagnie.objects.get(id=pk)
    vols=Vol.objects.all()
    return render(request,'compagnie/info.html',{'vols':vols,
                                                 'compagnies':compagnies})
