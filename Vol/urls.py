from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_vol,name='home_vol'),
    path('vol_info/<str:pk>',views.information,name='info-vol'),
]
