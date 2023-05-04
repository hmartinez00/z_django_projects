from django.core.management import execute_from_command_line

execute_from_command_line(['manage.py', 'makemigrations'])
execute_from_command_line(['manage.py', 'migrate'])
