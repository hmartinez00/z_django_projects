from django import template

register = template.Library()

@register.filter
def replace_spaces(value):
    new_value = value\
        .replace(' ', '_')\
        .replace('á', 'a')\
        .replace('é', 'e')\
        .replace('í', 'i')\
        .replace('ó', 'o')\
        .replace('ú', 'u')
        
    return new_value
