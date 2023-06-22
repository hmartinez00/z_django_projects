from General_Utilities.option_list import option_list
from ManageDB.sqlite_on_db import selectall_id, show_tables


database = r'CursoBsw3shools\db.sqlite3'
db_tables = show_tables(database)

tables = []
for i in db_tables:
    if 'BootStrap5_' in i:
        tables.append(i)

tabla = option_list(tables)

id = 'id'
df = selectall_id(database, tabla, id)['content']
for i in df:
    print(i)