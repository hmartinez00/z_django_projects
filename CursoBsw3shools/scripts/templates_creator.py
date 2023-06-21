import sys
import unicodedata

def remove_accents(value):
    normalized_value = unicodedata.normalize('NFKD', value)
    ascii_value = normalized_value.encode('ASCII', 'ignore').decode('utf-8')
    return ascii_value

def replace_spaces(value):
    new_value = remove_accents(value)\
        .replace(' ', '_')\
        .lower()
        
    return new_value


s = replace_spaces('ácento')
print(s)


# database = r"CursoBsw3shools\db.sqlite3"
# ruta_archivo_json = r'CursoBsw3shools\static\estructura_curso.json'

# with open(ruta_archivo_json, encoding='utf-8') as archivo_json:
#     datos_json = json.load(archivo_json)

# tables = list(datos_json.keys())
# values = []
# for i in datos_json[tables[0]]:
#     values.append(replace_spaces(i))

# print(tables, values)