from django.db import models

# Create your models here.
class Paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=12)
    apellido = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
    edad = models.IntegerField()
    genero = models.ForeignKey('Generos', models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'paciente'
class Doctor(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
    esp = models.ForeignKey('Especialidades', models.DO_NOTHING)
    edad = models.IntegerField()
    genero = models.ForeignKey('Generos', models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'doctor'
class Agenda(models.Model):
    agenda_id = models.AutoField(primary_key=True)
    doc_rut = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='doc_rut')
    pac_rut = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='pac_rut')
    agenda_dia = models.DateField()
    agenda_horai = models.TimeField(db_column='agenda_horaI')  # Field name made lowercase.
    agenda_horat = models.TimeField(db_column='agenda_horaT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agenda'
class Especialidades(models.Model):
    esp_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'especialidades'
class Generos(models.Model):
    gen_id = models.AutoField(primary_key=True)
    genero_nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'generos'
        
class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'
