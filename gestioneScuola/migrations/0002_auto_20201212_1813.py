# Generated by Django 3.1.4 on 2020-12-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneScuola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='voti1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='materia',
            name='voti2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
