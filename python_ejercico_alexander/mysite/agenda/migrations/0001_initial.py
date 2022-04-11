# Generated by Django 3.2.9 on 2021-12-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda_dia', models.DateField()),
                ('agenda_horai', models.TimeField(db_column='agenda_horaI')),
                ('agenda_horat', models.TimeField(db_column='agenda_horaT')),
            ],
            options={
                'db_table': 'agenda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=12)),
                ('edad', models.IntegerField()),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('esp_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'especialidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('gen_id', models.AutoField(primary_key=True, serialize=False)),
                ('genero_nombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'generos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=12)),
                ('apellido', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=12)),
                ('edad', models.IntegerField()),
            ],
            options={
                'db_table': 'paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
    ]