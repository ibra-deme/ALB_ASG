from django.contrib import admin
from .models import Compagnie


class Affichage(admin.ModelAdmin):
    list_display = ('nom','logo')
admin.site.register(Compagnie,Affichage)
# Register your models here.
