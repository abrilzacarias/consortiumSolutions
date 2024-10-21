from django.db import models
from django.db import connection
from django.utils.timezone import now
from django.utils import timezone


# Create your models here.
class EstadoFactura(models.Model):
    id_estado_factura = models.AutoField(primary_key=True)
    descripcion_estado_factura = models.CharField(max_length=50)

    class Meta:
        db_table = 'estado_factura'  # Nombre de la tabla en la base de datos
        managed = False 

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)  
    numero_comprobante = models.IntegerField()  
    fecha_emision = models.DateField(auto_now_add=True)
    id_venta = models.IntegerField() 
    id_tipo_factura = models.IntegerField()  # Puedes crear un modelo para tipos de factura
    link_descarga = models.CharField(max_length=500) 
    id_estado_factura = models.ForeignKey(EstadoFactura, default=1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'factura'  # Nombre de la tabla en la base de datos
        managed = False 


class DetalleFactura(models.Model):
    id_detalle_factura = models.AutoField(primary_key=True)   # Puede ser un ID único para cada detalle
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id_factura = models.IntegerField() 

    class Meta:
        db_table = 'detalle_factura'  # Nombre de la tabla en la base de datos
        managed = False 

class Facturas:
    
    @staticmethod

    def listarFacturas():
        with connection.cursor() as cursor:
            sqlListarPresupuestos = """
                    SELECT * FROM vista_facturas;
                    """
            cursor.execute(sqlListarPresupuestos)
            resultados = cursor.fetchall()
            
        return resultados



    def agregarFactura(numero_comprobante, id_venta, subtotal, total, link_descarga_factura):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO factura (numero_comprobante, fecha_emision_factura, id_venta, id_tipo_factura, link_descarga_factura)
                VALUES (%s, %s, %s, %s, %s)
            """, [numero_comprobante, timezone.now().date(), id_venta, 1, link_descarga_factura])
            id_factura = cursor.lastrowid
            connection.commit()

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO detalle_factura (subtotal, total, id_factura)
                VALUES (%s, %s, %s)
            """, [subtotal, total, id_factura])
            connection.commit()
