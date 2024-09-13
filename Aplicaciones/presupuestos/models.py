from django.db import models
from django.db import connection
from django.utils import timezone
from ..inicio.models import Edificio


current_datetime = timezone.localtime(timezone.now())

from django.db import models

class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    fecha_hora_presupuesto = models.DateTimeField()
    monto_total_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    id_empleado = models.IntegerField() 
    id_edificio = models.IntegerField()

    class Meta:
        db_table = 'presupuesto'  # Nombre de la tabla en la base de datos
        managed = False
        
    @classmethod
    def listarPresupuestos(cls):
        with connection.cursor() as cursor:
            sqlListarPresupuestos = """
                    SELECT pr.id_presupuesto, pr.fecha_hora_presupuesto, e.nombre_edificio, per.nombre_persona, pr.monto_total_presupuesto FROM presupuesto pr
                    JOIN edificio e ON e.id_edificio = pr.id_edificio
                    JOIN empleado emp ON emp.id_empleado = pr.id_empleado
                    JOIN persona per ON per.id_persona = emp.id_persona;
                    """
            cursor.execute(sqlListarPresupuestos)
            resultados = cursor.fetchall()
            presupuestos = []
        for resultado in resultados:
            presupuesto_modificado = {
                'id_presupuesto': resultado[0],
                'fecha_hora_presupuesto': resultado[1],
                'nombre_edificio': resultado[2],
                'nombre_persona': resultado[3],
                'monto_total_presupuesto': resultado[4]
            }
            presupuestos.append(presupuesto_modificado)
        return presupuestos
    
    
    def insertarPresupuesto(self, fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles):   
        try:
           
            with connection.cursor() as cursor:
                sqlInsertarPresupuesto = "INSERT INTO presupuesto (fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado ) VALUES (%s, %s, %s, %s);"
                cursor.execute(sqlInsertarPresupuesto, [fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado])
                id_presupuesto = cursor.lastrowid  
                connection.commit()


                for cantidad_detalle_presupuesto, precio_unitario_detalle_presupuesto, precio_total_detalle_presupuesto, id_servicio in lista_detalles:
                    sqlInsertarDetalle = "INSERT INTO detalle_presupuesto (cantidad_detalle_presupuesto, precio_unitario_detalle_presupuesto, precio_total_detalle_presupuesto, id_presupuesto, id_servicio) VALUES (%s, %s, %s, %s, %s);"
                    cursor.execute(sqlInsertarDetalle, [cantidad_detalle_presupuesto, precio_unitario_detalle_presupuesto, precio_total_detalle_presupuesto, id_presupuesto, id_servicio])
                    connection.commit()
      

                return id_presupuesto
        except Exception as e:
            print("Error al insertar:", str(e))
            return None

class DetallePresupuesto(models.Model):
    id_detalle_presupuesto = models.AutoField(primary_key=True)
    cantidad_detalle_presupuesto = models.IntegerField()
    precio_unitario_detalle_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    precio_total_detalle_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    id_presupuesto = models.ForeignKey('Presupuesto', models.DO_NOTHING, db_column='id_presupuesto')
    id_servicio = models.IntegerField()

    class Meta:
        db_table = 'detalle_presupuesto'
        managed = False  # Esto indica que Django no debería gestionar la creación de la tabla
    
    @classmethod
    def listarDetallePresupuesto(cls):
        with connection.cursor() as cursor:
            sqlListarDetallePresupuesto = """
                    SELECT dp.id_detalle_presupuesto, dp.cantidad_detalle_presupuesto, dp.precio_unitario_detalle_presupuesto, dp.precio_total_detalle_presupuesto, dp.id_presupuesto, dp.id_servicio, s.nombre_servicio
                    FROM detalle_presupuesto dp 
                    JOIN presupuesto p ON dp.id_presupuesto = p.id_presupuesto
                    JOIN servicio s ON dp.id_servicio = s.id_servicio;
                    """
            cursor.execute(sqlListarDetallePresupuesto)
            resultados = cursor.fetchall()
            detalle_presupuesto = []
        for resultado in resultados:
            detalle_presupuesto_modificado = {
            'id_detalle_presupuesto': resultado[0],
            'cantidad_detalle_presupuesto': resultado[1],
            'precio_unitario_detalle_presupuesto': resultado[2],
            'precio_total_detalle_presupuesto': resultado[3],
            'id_presupuesto': resultado[4],
            'id_servicio': resultado[5],
            'nombre_servicio': resultado[6]
            }
            detalle_presupuesto.append(detalle_presupuesto_modificado)
        return detalle_presupuesto