# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    doc_rut = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='doc_rut')
    pac_rut = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='pac_rut')
    agenda_dia = models.DateField()
    agenda_horai = models.TimeField(db_column='agenda_horaI')  # Field name made lowercase.
    agenda_horat = models.TimeField(db_column='agenda_horaT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agenda'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Paciente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=12)
    apellido = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
    edad = models.IntegerField()
    genero = models.ForeignKey(Generos, models.DO_NOTHING, db_column='genero')

    class Meta:
        managed = False
        db_table = 'paciente'


class Permiso(models.Model):
    per_id = models.AutoField(primary_key=True)
    rol = models.ForeignKey('Rol', models.DO_NOTHING)
    sec = models.ForeignKey('Secciones', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permiso'


class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


class Secciones(models.Model):
    sec_id = models.AutoField(primary_key=True)
    sec_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'secciones'


class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nombre = models.CharField("nombre",max_length=50)
    usu_pass = models.CharField("clave", max_length=50)
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column="rol_id")

    class Meta:
        managed = False
        db_table = 'usuario'
    def __str__(self):
        return self.usu_nombre
    
