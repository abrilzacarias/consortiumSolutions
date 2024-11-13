from django.db import models
from django.db import connection
from django.utils.timezone import now
from Aplicaciones.empleados.models import Empleado
from Aplicaciones.servicios.models import Servicio
from django.utils import timezone
from datetime import datetime


# Obtener la fecha y hora actual en la zona horaria local
current_datetime = timezone.localtime(timezone.now())
 

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

            # Verifica si la venta ya fue registrada en el diccionario
            if numero_factura not in ventas:
                ventas[numero_factura] = {
                    'id_venta': id_venta,
                    'numero_factura': numero_factura,
                    'fecha_hora_venta': resultado[2],
                    'nombre_edificio': resultado[3],
                    'cuit_edificio': resultado[4],
                    'direccion_edificio': resultado[5],
                    'id_metodo_pago': resultado[6],
                    'nombre_metodo_pago': resultado[7],
                    'cod_metodo_pago': resultado[8],
                    'nombre_empleado': resultado[9],
                    'monto_total_venta': resultado[10],
                    'detalles': []
                }

            # Crea un diccionario para el detalle de la venta
            detalle = {
                'id_detalle_venta': resultado[14],  # Posición del id_detalle_venta
                'nombre_servicio': resultado[11],
                'cantidad_detalle_venta': resultado[15],
                'precio_detalle_venta': resultado[13],
                'costo_extra_detalle_venta': resultado[16],
                'descripcion_estado_venta': resultado[18],
                'id_estado_venta': resultado[20],
                'observaciones': []  # Inicializa con una lista vacía
            }

            ids_observaciones = resultado[22].split(',') if resultado[22] else []  # Asegúrate de que el índice sea correcto
            descripciones_observaciones = resultado[23].split(', ') if resultado[23] else []
            fechas_observaciones = resultado[24].split(', ') if resultado[24] else []
            horas_observaciones = resultado[25].split(', ') if resultado[25] else []

            # Crea una lista de diccionarios para las observaciones
            observaciones = []
            for i in range(len(ids_observaciones)):
                # Solo agrega la observación si hay un id
                if ids_observaciones[i]:  # Asegúrate de que no esté vacío
                    observacion = {
                        'id_observacion': ids_observaciones[i],
                        'descripcion_observacion': descripciones_observaciones[i] if i < len(descripciones_observaciones) else None,
                        'fecha_observacion': fechas_observaciones[i] if i < len(fechas_observaciones) else None,
                        'hora_observacion': horas_observaciones[i] if i < len(horas_observaciones) else None,
                    }
                    observaciones.append(observacion)

            # Asigna las observaciones al detalle
            detalle['observaciones'] = observaciones

            # Agrega el detalle a la lista de detalles de la venta
            ventas[numero_factura]['detalles'].append(detalle)
            
            

        # Devuelve la lista de ventas
        return list(ventas.values())

                
    @classmethod
    def actualizarMetodoPago(cls, id_nuevo_metodo_pago, id_venta):
        with connection.cursor() as cursor:
            cursor.execute('''
                UPDATE venta
                SET id_metodo_pago = %s 
                WHERE id_venta = %s
            ''', [id_nuevo_metodo_pago, id_venta])  # Aquí se utiliza id_venta

        return cursor.rowcount > 0


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
    
    @classmethod
    def agregarObservacionDetalleVenta(cls, id_detalle_venta, descripcion_observacion, id_detalle_presupuesto=None, id_cliente=None):
        try:
            with connection.cursor() as cursor:
                sqlInsertarObservacionVenta = """
                    INSERT INTO observacion (descripcion_observacion, fecha_observacion, hora_observacion, id_detalle_venta, id_detalle_presupuesto, id_cliente)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """
                current_date = timezone.localtime(timezone.now()).date()
                current_time = timezone.localtime(timezone.now()).time()
                cursor.execute(sqlInsertarObservacionVenta, [descripcion_observacion, current_date, current_time, id_detalle_venta, id_detalle_presupuesto, id_cliente])
                idObservacion = cursor.lastrowid
                connection.commit()
                return idObservacion
        except Exception as e:
            print("Error al insertar:", str(e))
            return None


class RegistroEstadoVenta(models.Model):
    id_registro_estado_venta = models.AutoField(primary_key=True)
    fecha_hora_registro_estado_venta = models.DateTimeField(null=True, blank=True)
    id_detalle_venta = models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, db_column='id_detalle_venta')
    id_estado_venta = models.ForeignKey('EstadoVenta', null=True, blank=True, on_delete=models.SET_NULL, db_column='id_estado_venta')
    fecha_baja_estado = models.DateField(null=True, blank=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, db_column='id_empleado')

    class Meta:
        db_table = 'registro_estado_venta'
        managed = False

    @classmethod
    def registrarCambioEstado(cls, id_detalle_venta, id_estado_venta, id_empleado):
        # Actualiza la fecha de baja del estado anterior
        with connection.cursor() as cursor:
            cursor.execute('''
                UPDATE registro_estado_venta
                SET fecha_baja_estado = NOW()
                WHERE id_detalle_venta = %s AND fecha_baja_estado IS NULL
            ''', [id_detalle_venta])
        
        # Inserta el nuevo estado
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO registro_estado_venta (fecha_hora_registro_estado_venta, id_detalle_venta, id_estado_venta, id_empleado, fecha_baja_estado)
                VALUES (NOW(), %s, %s, %s, NULL)
            ''', [id_detalle_venta, id_estado_venta, id_empleado])

class EstadoVenta(models.Model):
    id_estado_venta = models.AutoField(primary_key=True)
    descripcion_estado_venta = models.CharField(max_length=45)

    class Meta:
        db_table = 'estado_venta'  # Nombre de la tabla en la base de datos
        managed = False  # Esto indica que Django no debe crear ni modificar esta tabla
    
    @classmethod
    def obtenerEstadosVenta(cls):
        # Obtener todos los estados de venta
        estados = cls.objects.all()
        # Retornar una lista de diccionarios con id y descripción
        return [{'id': estado.id_estado_venta, 'nombre': estado.descripcion_estado_venta} for estado in estados]
