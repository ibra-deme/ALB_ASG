from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def home_trajet(request):
    trajets=Trajet.objects.all()
    return  render(request,'trajet/trajet.html',{'trajets':trajets})

