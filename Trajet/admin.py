from django.contrib import admin
from .models import Trajet


class Affichage(admin.ModelAdmin):
    list_display = ('depart','arrive')
admin.site.register(Trajet,Affichage)
# Register your models here.
