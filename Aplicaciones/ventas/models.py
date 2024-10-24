from django.db import models
from django.db import connection
from django.utils.timezone import now
from Aplicaciones.empleados.models import Empleado
from Aplicaciones.servicios.models import Servicio

class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=70)
    cod_metodo_pago = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'metodo_pago'  # Nombre de la tabla en la base de datos
        managed = False  # Esto indica que Django no debe crear ni modificar esta tabla
    
    @classmethod
    def obtenerMetodosPago(cls):
        # Obtener todos los métodos de pago
        metodos = cls.objects.all()  
        # Retornar una lista de diccionarios con id y nombre
        return [{'id': metodo.id_metodo_pago, 'nombre': metodo.nombre_metodo_pago} for metodo in metodos]


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)  # id_venta es la clave primaria
    numero_factura = models.CharField(max_length=45)  # Campo varchar de longitud 45
    fecha_hora_venta = models.DateTimeField()  # Campo datetime
    monto_total_venta = models.DecimalField(max_digits=10, decimal_places=0)  # Campo decimal (10,0)
    id_edificio = models.IntegerField()  # id_edificio es un índice (campo entero)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE, null=True, db_column='id_metodo_pago')  # Modificado
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
                    'id_detalle_venta': resultado[13],  # Agregado
                    'nombre_servicio': resultado[10],
                    'cantidad_detalle_venta': resultado[11],
                    'precio_detalle_venta': resultado[12],
                    'costo_extra_detalle_venta': resultado[15],  # Agregado
                    'descripcion_estado_venta': resultado[17],  # Descripción del estado de venta
                }
                ventas[numero_factura]['detalles'].append(detalle)

            return list(ventas.values())
        
    @classmethod
    def actualizarMetodoPago(cls, id_nuevo_metodo_pago, id_venta):
        with connection.cursor() as cursor:
            cursor.execute('''
                UPDATE venta
                SET id_metodo_pago = %s 
                WHERE id_venta = %s
            ''', [id_nuevo_metodo_pago, id_venta])  # Aquí se utiliza id_venta




# Llamada al método para probarlo
#hola = MetodoPago.obtenerMetodosPago()

class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    cantidad_detalle_venta = models.IntegerField()
    costo_extra_detalle_venta = models.DecimalField(max_digits=10, decimal_places=0)
    precio_total_detalle_venta = models.DecimalField(max_digits=10, decimal_places=0)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)  # Relación con Venta
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)  # Relación corregida con Servicio

    def _str_(self):
        return f'Detalle Venta {self.id_detalle_venta}'

class RegistroEstadoVenta(models.Model):
    id_registro_estado_venta = models.AutoField(primary_key=True)
    fecha_hora_registro_estado_venta = models.DateTimeField(null=True, blank=True)
    id_detalle_venta = models.ForeignKey(DetalleVenta, on_delete=models.CASCADE)  # Relación con DetalleVenta
    id_estado_venta = models.ForeignKey('EstadoVenta', null=True, blank=True, on_delete=models.SET_NULL)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  # Relación corregida con Empleado

    def _str_(self):
        return f'Registro Estado Venta {self.id_registro_estado_venta}'

class EstadoVenta(models.Model):
    id_estado_venta = models.AutoField(primary_key=True)
    descripcion_estado_venta = models.CharField(max_length=45)

    def _str_(self):
        return self.descripcion_estado_venta