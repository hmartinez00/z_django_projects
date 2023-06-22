import os
import sys
import json


def normalizar(value):
    str_string = str(str(value).lower())
    replacements = {
        ' ': '_',
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
    }
    new_value = ''
    for char in str_string:
        if char in replacements:
            new_value += replacements[char]
        else:
            new_value += char
    return new_value

valor = 'BS5 Rejílla Básica'
print(normalizar(valor))