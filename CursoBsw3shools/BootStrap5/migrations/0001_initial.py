# Generated by Django 4.2 on 2023-06-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap_5_formularios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=1)),
                ('youtube_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bootstrap_5_Otros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=1)),
                ('youtube_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=1)),
                ('youtube_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rejilla_Bootstrap_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=1)),
                ('youtube_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial_de_Bootstrap_5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.IntegerField(default=1)),
                ('youtube_url', models.CharField(max_length=100)),
            ],
        ),
    ]