from django.db import models
from django.db import connection
from django.utils.timezone import now
from django.db import models

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)  # id_venta es la clave primaria
    numero_factura = models.CharField(max_length=45)  # Campo varchar de longitud 45
    fecha_hora_venta = models.DateTimeField()  # Campo datetime
    monto_total_venta = models.DecimalField(max_digits=10, decimal_places=0)  # Campo decimal (10,0)
    id_edificio = models.IntegerField()  # id_edificio es un índice (campo entero)
    id_metodo_pago = models.IntegerField()  # id_metodo_pago es un índice (campo entero)
    id_empleado = models.IntegerField()  # id_empleado es un índice (campo entero)
    id_presupuesto = models.IntegerField()  # id_presupuesto es un índice (campo entero)

    class Meta:
        db_table = 'venta'  # Nombre de la tabla en la base de datos
        managed = False  # Esto indica que Django no debe crear ni modificar esta tabla

    @classmethod
    def listarVentas(cls):
        with connection.cursor() as cursor:
            sqlListarVentas = """
                    SELECT * FROM vista_ventas;
                    """
            cursor.execute(sqlListarVentas)
            resultados = cursor.fetchall()
            ventas = []
            
            for resultado in resultados:
                venta_modificada = {
                    'numero_factura': resultado[0],
                    'fecha_hora_venta': resultado[1],
                    'nombre_edificio': resultado[2],
                    'cuit_edificio': resultado[3],
                    'direccion_edificio': resultado[4],
                    'nombre_metodo_pago': resultado[5],
                    'cod_metodo_pago': resultado[6],
                    'nombre_empleado': resultado[7],
                    'monto_total_venta': resultado[8],
                    'nombre_servicio': resultado[9],
                    'cod_servicio': resultado[10],
                    'precio': resultado[11],
                    'cantidad_detalle_venta': resultado[12],
                    'costo_extra_detalle_venta': resultado[13],
                    'fecha_hora_registro_estado_venta': resultado[14],
                    'descripcion_estado_venta': resultado[15],
                }
                ventas.append(venta_modificada)
        return ventas

            