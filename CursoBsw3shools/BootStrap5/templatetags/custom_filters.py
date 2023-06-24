from django import template
import unidecode
import re

register = template.Library()

@register.filter
def replace_spaces(string):
    new_string = unidecode.unidecode(string).lower()
    return new_string.replace(' ', '_')

@register.filter
def extract_numbers(string):
    numbers = re.findall(r'\d+', string)
    numbers = int(numbers[0])
    return numbers
