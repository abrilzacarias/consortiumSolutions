# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models, connection


class CategoriaServicio(models.Model):
    id_categoria_servicio = models.AutoField(primary_key=True)
    nombre_categoria_servicio = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria_servicio'

    @staticmethod
    def agregarCategoria(nombreCategoria):
        categoria = nombreCategoria.capitalize()
        try:
            with connection.cursor() as cursor:
                sqlconsulta = "INSERT INTO categoria_servicio (nombre_categoria_servicio) VALUES (%s);"
                cursor.execute(sqlconsulta, [categoria])
                idCategoria = cursor.lastrowid  # Esto obtiene el ID en la mayoría de las bases de datos
                connection.commit()
                return idCategoria
        except Exception as e:
            print("Error al insertar:", str(e))
            return None


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=45, blank=True, null=True)
    requiere_pago_servicio = models.IntegerField(blank=True, null=True)
    id_categoria_servicio = models.ForeignKey(CategoriaServicio, models.DO_NOTHING, db_column='id_categoria_servicio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'
