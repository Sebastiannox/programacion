# Generated by Django 3.2.9 on 2021-11-22 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20211119_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_test',
            name='columna_dos',
        ),
        migrations.RemoveField(
            model_name='table_test',
            name='columna_tres',
        ),
    ]