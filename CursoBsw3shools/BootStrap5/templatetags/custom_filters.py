from django import template

register = template.Library()

@register.filter
def replace_spaces(s):
    replacements = (
        (" ", "_"),
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = str(s).replace(a, b)
    return s.lower()
