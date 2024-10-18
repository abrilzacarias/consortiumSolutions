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
        
from django.db import models
from django.db import connection

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
            print(resultados)
            ventas = {}

            for resultado in resultados:
                numero_factura = resultado[1]  # Suponiendo que el número de factura es el segundo elemento
                id_venta = resultado[0]         # Primer elemento es el id_venta
                id_detalle_venta = resultado[12] # Posición del id_detalle_venta

                if numero_factura not in ventas:
                    ventas[numero_factura] = {
                        'id_venta': id_venta,  # Agregado
                        'numero_factura': numero_factura,
                        'fecha_hora_venta': resultado[2],
                        'nombre_edificio': resultado[3],
                        'cuit_edificio': resultado[4],
                        'direccion_edificio': resultado[5],
                        'nombre_metodo_pago': resultado[6],
                        'cod_metodo_pago': resultado[7],
                        'nombre_empleado': resultado[8],
                        'monto_total_venta': resultado[9],
                        'detalles': []
                    }

                detalle = {
                    'id_detalle_venta': id_detalle_venta,  # Agregado
                    'nombre_servicio': resultado[10],
                    'cantidad_detalle_venta': resultado[11],
                    'precio_detalle_venta': resultado[12],
                    'costo_extra_detalle_venta': resultado[15],  # Agregado
                    'descripcion_estado_venta': resultado[17],  # Descripción del estado de venta
                }
                ventas[numero_factura]['detalles'].append(detalle)

            return list(ventas.values())



                