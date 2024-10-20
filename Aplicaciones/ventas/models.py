from django.db import models
from django.db import connection
from django.utils.timezone import now


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
    def editarVenta(cls, id_presupuesto, nuevo_monto_total, nuevo_id_edificio, nuevo_id_empleado, lista_detalles):
        try:
            current_datetime = now()

            with connection.cursor() as cursor:
                # Actualizar el presupuesto principal
                sqlActualizarPresupuesto = """
                    UPDATE presupuesto
                    SET fecha_hora_presupuesto = %s,
                        monto_total_presupuesto = %s,
                        id_edificio = %s,
                        id_empleado = %s
                    WHERE id_presupuesto = %s;
                """
                cursor.execute(sqlActualizarPresupuesto, [current_datetime, nuevo_monto_total, nuevo_id_edificio, nuevo_id_empleado, id_presupuesto])

                # Procesar los detalles
                for detalle in lista_detalles:
                    if detalle['id_detalle_presupuesto'] == 'null':
                        detalle['id_detalle_presupuesto'] = None
                        
                    if detalle['id_detalle_presupuesto']:
                        # Actualizar el detalle si ya existe
                        sqlActualizarDetalle = """
                            UPDATE detalle_presupuesto
                            SET cantidad_detalle_presupuesto = %s,
                                costo_extra_presupuesto = %s,
                                precio_total_detalle_presupuesto = %s
                            WHERE id_presupuesto = %s AND id_servicio = %s;
                        """
                        cursor.execute(sqlActualizarDetalle, [detalle['cantidad'], detalle['costos_extra'], detalle['precio_total'], id_presupuesto, detalle['id_servicio']])
                    else:
                        # Insertar nuevo detalle si no existe
                        sqlInsertarDetalle = """
                            INSERT INTO detalle_presupuesto
                            (cantidad_detalle_presupuesto, costo_extra_presupuesto, precio_total_detalle_presupuesto, id_presupuesto, id_servicio)
                            VALUES (%s, %s, %s, %s, %s);
                        """
                        cursor.execute(sqlInsertarDetalle, [detalle['cantidad'], detalle['costos_extra'], detalle['precio_total'], id_presupuesto, detalle['id_servicio']])
                
                connection.commit()
                print("Actualización y commit completados con éxito")
            return True
        except Exception as e:
            print("Error al actualizar presupuesto:", str(e))
            return False


    def editarVenta(request):
        if request.method == 'POST':
            id_presupuesto = request.POST.get('id_presupuesto')
            monto_total_presupuesto = request.POST.get('totalCostEditar')
            id_edificio = request.POST.get('edificio_asignado_editar')
            id_empleado = request.POST.get('vendedor_asignado_editar')

            lista_cantidad_detalle_presupuesto = request.POST.getlist('cantidades_editar[]')
            costos_extra = request.POST.getlist('costos_extra_editar[]')
            lista_precio_total_detalle_presupuesto = request.POST.getlist('subtotales_editar[]')
            lista_id_servicio = request.POST.getlist('servicios_editar[]')
            lista_id_detalles = request.POST.getlist('id_detalles_editar[]')

            # Lógica para crear la lista de detalles del presupuesto
            lista_detalles = [
                {
                    'id_detalle_presupuesto': id_detalle,
                    'id_servicio': id_servicio,
                    'cantidad': cantidad,
                    'costos_extra': costo_extra,
                    'precio_total': precio_total
                }
                for id_detalle, id_servicio, cantidad, costo_extra, precio_total in zip(
                    lista_id_detalles,
                    lista_id_servicio,
                    lista_cantidad_detalle_presupuesto,
                    costos_extra,
                    lista_precio_total_detalle_presupuesto
                )
            ]

            # Obtener el tipo de acción: editar o enviar a ventas
            action_type = request.POST.get('action_type')

            if action_type == 'editar':
                # Si el botón presionado es "Editar Presupuesto"
                resultado = Presupuesto.actualizarPresupuesto(id_presupuesto, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles)
                if resultado:
                    messages.success(request, 'El presupuesto se actualizó correctamente.')
                else:
                    messages.error(request, 'Hubo un error al actualizar el presupuesto.')
                return redirect('/presupuestos/')

            elif action_type == 'enviarVentas':
                # Redirigir a la vista de enviar a ventas
                return redirect('presupuestos:enviarVentas', id_presupuesto=id_presupuesto)

        return redirect('/presupuestos/')