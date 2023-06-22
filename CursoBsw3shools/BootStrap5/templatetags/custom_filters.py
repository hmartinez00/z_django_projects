from django import template
import unidecode

register = template.Library()

@register.filter
def replace_spaces(string):
    new_string = unidecode.unidecode(string).replace(' ', '_').lower()
    return new_string
