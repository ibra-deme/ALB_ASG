from django.shortcuts import render
def home(request):
    return  render(request,'dashboard/tour/index.html')
# Create your views here.
