from django.contrib import admin
from .models import MenuObj


@admin.register(MenuObj)
class MenuObjAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'url']

