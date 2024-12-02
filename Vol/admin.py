from django.contrib import admin
from .models import Vol

class Affichage(admin.ModelAdmin):
    list_display = ('prix','date','heure')
admin.site.register(Vol,Affichage)
# Register your models here.
