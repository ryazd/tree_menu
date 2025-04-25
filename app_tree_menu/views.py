from django.shortcuts import render
from .models import MenuObj


def draw_menu(request, menu_name):
    return render(request, 
                'app_tree_menu/list.html', 
                {'menu_name': menu_name})