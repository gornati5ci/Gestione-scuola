# Generated by Django 3.1.4 on 2020-12-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioneScuola', '0004_voto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quadrimestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quadrimestre', models.IntegerField()),
            ],
        ),
    ]