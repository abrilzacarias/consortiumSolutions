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
                idCategoria = cursor.lastrowid  
                connection.commit()
                return idCategoria
        except Exception as e:
            print("Error al insertar:", str(e))
            return None
        
    def aumentarPrecio(self, id_categoria, porcentaje):
        try:
            with connection.cursor() as cursor:
                cursor.callproc('aumentar_precio_categoria', [id_categoria, porcentaje])
                connection.commit()
                return True
        except Exception as e:
            print("Error al aumentar el precio:", str(e))
            return False


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=70)
    requiere_pago_servicio = models.IntegerField()
    precio_base_servicio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    id_categoria_servicio = models.ForeignKey(CategoriaServicio, models.DO_NOTHING, db_column='id_categoria_servicio')

    class Meta:
        managed = False
        db_table = 'servicio'
        
