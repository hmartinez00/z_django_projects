from django import template

register = template.Library()

@register.filter
def normalizar(string):
    replacements = {
        ' ': '_',
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    new_string = ''
    for char in string:
        if char in replacements:
            new_string += replacements[char]
        else:
            new_string += char
    return new_string.lower()
