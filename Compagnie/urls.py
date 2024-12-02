from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home_compagnie,name='home_compagnie'),
    path('modifier/<str:pk>',views.modifier_compagnie,name='modifier_compagnie'),
    path('information/<str:pk>',views.information,name='information'),
]
