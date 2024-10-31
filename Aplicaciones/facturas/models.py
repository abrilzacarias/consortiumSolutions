from django.db import models
from django.db import connection
from django.utils.timezone import now
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail


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
    fecha_emision_factura = models.DateField(auto_now_add=True)
    id_venta = models.IntegerField() 
    id_tipo_factura = models.IntegerField()  # Puedes crear un modelo para tipos de factura
    link_descarga_factura = models.CharField(max_length=500) 
    id_estado_factura = models.ForeignKey(EstadoFactura, default=1, on_delete=models.CASCADE, db_column='id_estado_factura')

    class Meta:
        db_table = 'factura'  # Nombre de la tabla en la base de datos
        managed = False 
    
    @classmethod
    def listarFacturas(cls):
        with connection.cursor() as cursor:
            sqlListarFacturas = """
                    SELECT * FROM vista_facturas;
                    """
            cursor.execute(sqlListarFacturas)
            resultados = cursor.fetchall()

            # Diccionario para almacenar las facturas agrupadas por número de comprobante
            facturas = {}

            for resultado in resultados:
                numero_comprobante = resultado[1]  # Asumimos que el número de comprobante es el segundo elemento
                id_factura = resultado[0]          # Primer elemento es el id_factura
                id_detalle_factura = resultado[12]  # Posición del id_detalle_factura

                # Si el número de comprobante aún no está en el diccionario, inicializamos su estructura
                if numero_comprobante not in facturas:
                    facturas[numero_comprobante] = {
                        'id_factura': id_factura,
                        'numero_comprobante': numero_comprobante,
                        'fecha_emision_factura': resultado[2],
                        'nombre_cliente': resultado[3],
                        'apellido_cliente': resultado[4],
                        'nombre_edificio': resultado[5],
                        'descarga_ticket': resultado[6],
                        'id_estado_factura': resultado[7],
                        'descripcion_estado_factura': resultado[8],
                        'detalles': []  # Lista para agregar los detalles de cada servicio
                    }
                
                # Agregamos cada servicio como un detalle separado
                facturas[numero_comprobante]['detalles'].append({
                    'nombre_servicio': resultado[9],
                    'cantidad_servicio': resultado[10],
                    'precio_total_servicio': resultado[11],
                    'correo_cliente': resultado[12],
                    'metodo_pago': resultado[13], 
                    'nombre_metodo_pago': resultado[14]
                })

        return list(facturas.values())

    def agregarFactura(numero_comprobante, id_venta, subtotal, total, link_descarga_factura, id_estado_factura):
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO factura (numero_comprobante, fecha_emision_factura, id_venta, id_tipo_factura, link_descarga_factura, id_estado_factura)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, [numero_comprobante, timezone.now().date(), id_venta, 1, link_descarga_factura, id_estado_factura])
            id_factura = cursor.lastrowid
            connection.commit()

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO detalle_factura (subtotal, total, id_factura)
                VALUES (%s, %s, %s)
            """, [subtotal, total, id_factura])
            connection.commit()

    def obtenerUltimoComprobanteFactura(): 
        with connection.cursor() as cursor:
            sqlObtenerComprobante = """
                    SELECT 
                        MAX(numero_comprobante) AS ultimo_numero_comprobante
                    FROM 
                        factura;
                    """
            cursor.execute(sqlObtenerComprobante)
            resultados = cursor.fetchall()
        return resultados
    
    def enviar_correo_link_pago(correo_electronico, link_pago, nombre_cliente, apellido_cliente, descarga_ticket):
        asunto = 'Link de Pago de su Compra'
        mensaje = (
            f'Hola {apellido_cliente} {nombre_cliente}! \n'
            f'A continuación se deja el link de pago de Mercado Pago:\n'
            f'{link_pago}\n'
            f'Por favor, recuerde enviar el comprobante de pago.\n'
            f'Puedes descargar tu ticket aquí: {descarga_ticket}\n'
        )
        remitente = settings.EMAIL_HOST_USER 

        # Enviar el correo
        send_mail(asunto, mensaje, remitente, [correo_electronico])


class DetalleFactura(models.Model):
    id_detalle_factura = models.AutoField(primary_key=True)   # Puede ser un ID único para cada detalle
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id_factura = models.IntegerField() 

    class Meta:
        db_table = 'detalle_factura'  # Nombre de la tabla en la base de datos
        managed = False 




#resultado = Facturas.listarFacturas()