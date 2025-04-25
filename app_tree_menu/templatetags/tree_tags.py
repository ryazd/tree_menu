from django import template
from ..models import MenuObj
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuObj.objects.filter(url=menu_name).select_related('parent')
    lst = get_parents(menu_items[0])
    resp = make_menu(MenuObj.objects.filter(url='main_menu'), lst)
    return mark_safe(resp)


def get_parents(menu_item):
    lst = [menu_item]
    item = menu_item.parent
    while item:
        lst.append(item)
        item = item.parent    
    return lst


def make_menu(menu_items, lst):
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.get_absolute_url()}">{item.title}</a>'
        else:
            menu_html += item.title
        if item in lst and item.children.exists():
            menu_html += make_menu(item.children.all(), lst)
        menu_html += '</li>'
    menu_html += '</ul>'  
    return menu_html

    


    

    