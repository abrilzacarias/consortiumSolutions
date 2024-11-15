from django.db import models
from django.db import connection
from django.utils.timezone import now
from django.utils import timezone
from datetime import datetime
        
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
                    SELECT pr.id_presupuesto, pr.fecha_hora_presupuesto, e.nombre_edificio, CONCAT(per.nombre_persona, ' ', per.apellido_persona) AS nombre_empleado, pr.monto_total_presupuesto, pr.estado_presupuesto, emp.id_empleado FROM presupuesto pr
                    JOIN edificio e ON e.id_edificio = pr.id_edificio
                    JOIN empleado emp ON emp.id_empleado = pr.id_empleado
                    JOIN persona per ON per.id_persona = emp.id_persona
                    WHERE pr.estado_presupuesto = 0;
                    """
            cursor.execute(sqlListarPresupuestos)
            resultados = cursor.fetchall()
            presupuestos = []
        for resultado in resultados:
            presupuesto_modificado = {
                'id_presupuesto': resultado[0],
                'fecha_hora_presupuesto': resultado[1],
                'nombre_edificio': resultado[2],
                'nombre_empleado': resultado[3],
                'monto_total_presupuesto': resultado[4],
                'id_empleado': resultado[6],
            }
            presupuestos.append(presupuesto_modificado)
        return presupuestos
    
    @classmethod
    def insertarPresupuesto(cls, monto_total_presupuesto, id_edificio, id_empleado, lista_detalles):   
        current_datetime = now()  # Obtener la fecha y hora actual
        try:
            with connection.cursor() as cursor:
                sqlInsertarPresupuesto = "INSERT INTO presupuesto (fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado ) VALUES (%s, %s, %s, %s);"
                cursor.execute(sqlInsertarPresupuesto, [current_datetime, monto_total_presupuesto, id_edificio, id_empleado])
                id_presupuesto = cursor.lastrowid  
                connection.commit()


                for detalle in lista_detalles:
                    sqlInsertarDetalle = "INSERT INTO detalle_presupuesto (cantidad_detalle_presupuesto, costo_extra_presupuesto, precio_total_detalle_presupuesto, id_presupuesto, id_servicio) VALUES (%s, %s, %s, %s, %s);"
                    cursor.execute(sqlInsertarDetalle, [detalle['cantidad'], detalle['costo_extra_presupuesto'], detalle['precio_total'], id_presupuesto, detalle['id_servicio']])
                    connection.commit()
                
                print(id_presupuesto)
                return id_presupuesto
        except Exception as e:
            print("Error al insertar:", str(e))
            return None

    @classmethod
    def actualizarPresupuesto(cls, id_presupuesto, nuevo_monto_total, nuevo_id_edificio, nuevo_id_empleado, lista_detalles):
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
        
    def generarNumeroFactura():
        # Obtener el número secuencial más alto ya existente en la base de datos
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(numero_factura) FROM venta;")
            resultado = cursor.fetchone()
            if resultado[0] is not None:
                ultimo_numero_factura = int(resultado[0].split('-')[1])  # Extraer el número
            else:
                ultimo_numero_factura = 0  # Si no hay facturas, empezar en 0

        nuevo_numero_factura = ultimo_numero_factura + 1  # Incrementar el número secuencial
        return f"FACT-{str(nuevo_numero_factura).zfill(3)}"  # Formato FACT-001


    @classmethod
    def enviarVentas(cls, id_presupuesto):
        try:
            # Obtener el presupuesto y sus detalles
            with connection.cursor() as cursor:
                # Consulta para obtener el presupuesto
                sqlPresupuesto = """
                    SELECT id_presupuesto, fecha_hora_presupuesto, monto_total_presupuesto, id_edificio, id_empleado 
                    FROM presupuesto
                    WHERE id_presupuesto = %s;
                """
                cursor.execute(sqlPresupuesto, [id_presupuesto])
                presupuesto = cursor.fetchone()
                        
                if presupuesto:
                    # Obtener el id_cliente a partir del id_edificio
                    sqlObtenerCliente = """
                        SELECT id_cliente 
                        FROM edificio
                        WHERE id_edificio = %s;
                    """
                    cursor.execute(sqlObtenerCliente, [presupuesto[3]])  # `presupuesto[3]` es el `id_edificio`
                    cliente_id = cursor.fetchone()

                    if cliente_id:
                        id_cliente = cliente_id[0]  # Extraer el valor del `id_cliente`
                        print("id_cliente:", id_cliente)  # Para verificar qué `id_cliente` está llegando

                        # Verificar y actualizar `conversion_cliente` si es necesario
                        sqlVerificarCliente = """
                            SELECT conversion_cliente 
                            FROM cliente 
                            WHERE id_cliente = %s;
                        """
                        cursor.execute(sqlVerificarCliente, [id_cliente])
                        cliente = cursor.fetchone()

                        if cliente and cliente[0] == 0:  # Si `conversion_cliente` es 0
                            sqlActualizarConversion = """
                                UPDATE cliente 
                                SET conversion_cliente = 1 
                                WHERE id_cliente = %s;
                            """
                            cursor.execute(sqlActualizarConversion, [id_cliente])

                    # Generar número de factura en el formato FACT-001
                    numeroFactura = cls.generarNumeroFactura()  

                    # Insertar el presupuesto en la tabla de ventas
                    sqlInsertarVenta = """
                        INSERT INTO venta (numero_factura, fecha_hora_venta, monto_total_venta, id_edificio, id_empleado, id_presupuesto)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """
                    cursor.execute(sqlInsertarVenta, [numeroFactura, presupuesto[1], presupuesto[2], presupuesto[3], presupuesto[4], id_presupuesto])
                    id_venta = cursor.lastrowid

                    # Obtener los detalles del presupuesto
                    sqlDetallePresupuesto = """
                        SELECT id_detalle_presupuesto, cantidad_detalle_presupuesto, costo_extra_presupuesto, precio_total_detalle_presupuesto, id_servicio
                        FROM detalle_presupuesto
                        WHERE id_presupuesto = %s;
                    """
                    cursor.execute(sqlDetallePresupuesto, [id_presupuesto])
                    detalles_presupuesto = cursor.fetchall()

                    # Insertar los detalles en detalle_venta
                    for detalle in detalles_presupuesto:
                        sqlInsertarDetalleVenta = """
                            INSERT INTO detalle_venta (cantidad_detalle_venta, costo_extra_detalle_venta, precio_total_detalle_venta, id_venta, id_servicio)
                            VALUES (%s, %s, %s, %s, %s);
                        """
                        cursor.execute(sqlInsertarDetalleVenta, [detalle[1], detalle[2], detalle[3], id_venta, detalle[4]])

                        id_detalle_venta = cursor.lastrowid  # Obtener el último ID de detalle_venta insertado

                        # Insertar en la tabla intermedia de estado de venta
                        sqlInsertarEstadoVenta = """
                            INSERT INTO registro_estado_venta (fecha_hora_registro_estado_venta, id_detalle_venta, id_estado_venta, id_empleado)
                            VALUES (%s, %s, %s, %s);
                        """
                        try:
                            cursor.execute(sqlInsertarEstadoVenta, [
                                None,  # fecha_hora_registro_estado_venta inicial nulo
                                id_detalle_venta, 
                                None,  # id_estado_venta inicial nulo
                                presupuesto[4]  # Asignar id_empleado
                            ])
                        except Exception as e:
                            print("Error al insertar en registro_estado_venta:", str(e))

                    # Confirmar las transacciones
                    connection.commit()

                    return id_venta
                else:
                    print("No se encontró el presupuesto.")
                    return None
        except Exception as e:
            print("Error al enviar ventas:", str(e))
            connection.rollback()
            return None

    
    @classmethod
    def filtrarVendedores(self):
        #filtra los vendedores que no tienen fecha de baja, es decir, que estan activos
        try:
            with connection.cursor() as cursor:
                sqlVendedoresActivos = """
                    SELECT 
                        e.id_empleado,
                        p.nombre_persona,
                        p.apellido_persona
                    FROM 
                            empleado e
                        JOIN 
                            persona p ON e.id_persona = p.id_persona  
                        LEFT JOIN 
                            login_myuser_groups g ON e.id_usuario = g.myuser_id  
                        LEFT JOIN 
                            auth_group ag ON g.group_id = ag.id  
                        WHERE 
                            e.fecha_baja_empleado IS NULL
                    AND 
                        ag.name = 'Vendedor';
                                    """
                cursor.execute(sqlVendedoresActivos)
                vendedoresActivos = cursor.fetchall()
                
                connection.commit()
                return vendedoresActivos
        except Exception as e:
            print("Error al enviar ventas:", str(e))
            connection.rollback()
            return None

class Observacion(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    descripcion_observacion = models.CharField(max_length=2000)
    fecha_observacion = models.DateField()
    hora_observacion = models.TimeField()
    id_detalle_presupuesto = models.ForeignKey('DetallePresupuesto', on_delete=models.CASCADE, related_name='observaciones',db_column='id_detalle_presupuesto')

    class Meta:
        db_table = 'observacion'

    
    @classmethod
    def listarObservaciones(cls, id_detalle_presupuesto):
        with connection.cursor() as cursor:
            sqlListarObservaciones = """
                SELECT 
                    o.id_observacion,
                    o.descripcion_observacion,
                    o.fecha_observacion,
                    o.hora_observacion,
                    CONCAT(p.nombre_persona, ' ', p.apellido_persona) AS nombre_completo
                FROM observacion o
                JOIN empleado e ON o.id_empleado = e.id_empleado
                JOIN persona p ON e.id_persona = p.id_persona
                WHERE o.id_detalle_presupuesto = %s;
            """
            cursor.execute(sqlListarObservaciones, [id_detalle_presupuesto])
            resultados = cursor.fetchall()
            observaciones = []

        for resultado in resultados:
            observaciones.append({
                'id_observacion': resultado[0],
                'descripcion_observacion': resultado[1],
                'fecha_observacion': resultado[2],
                'hora_observacion': resultado[3],
                'nombre_observador': resultado[4],
            })

        return observaciones



class DetallePresupuesto(models.Model):
    id_detalle_presupuesto = models.AutoField(primary_key=True)
    cantidad_detalle_presupuesto = models.IntegerField()
    costo_extra_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
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
                SELECT 
                    dp.id_detalle_presupuesto, 
                    dp.cantidad_detalle_presupuesto, 
                    dp.costo_extra_presupuesto, 
                    dp.precio_total_detalle_presupuesto, 
                    dp.id_presupuesto, 
                    dp.id_servicio, 
                    s.nombre_servicio,
                    s.precio_base_servicio
                FROM detalle_presupuesto dp 
                JOIN presupuesto p ON dp.id_presupuesto = p.id_presupuesto
                JOIN servicio s ON dp.id_servicio = s.id_servicio;
            """
            cursor.execute(sqlListarDetallePresupuesto)
            resultados = cursor.fetchall()
            
            print(f"Resultados de la consulta: {resultados}")  # Imprime los resultados de la consulta
            
            detalle_presupuesto = []
            
            for resultado in resultados:
                # Obtener las observaciones para cada detalle
                observaciones = Observacion.listarObservaciones(resultado[0])  # Aquí pasas el id_detalle_presupuesto
                
                detalle_presupuesto_modificado = {
                    'id_detalle_presupuesto': resultado[0],
                    'cantidad_detalle_presupuesto': resultado[1],
                    'costo_extra_presupuesto': resultado[2],
                    'precio_total_detalle_presupuesto': resultado[3],
                    'id_presupuesto': resultado[4],
                    'id_servicio': resultado[5],
                    'nombre_servicio': resultado[6],
                    'precio_servicio': float(resultado[7]) if resultado[7] is not None else 0.0,  # Agrega 0.0 si es None
                    'observaciones': observaciones  # Agrega las observaciones
                }
                detalle_presupuesto.append(detalle_presupuesto_modificado)
        
        return detalle_presupuesto
    
    
        

    @classmethod
    def agregarObservacionPresupuesto(cls, id_detalle_presupuesto, descripcion_observacion, id_empleado, id_detalle_venta=None, id_cliente=None):
        try:
            with connection.cursor() as cursor:
                sqlInsertarObservacionPresupuesto = """
                    INSERT INTO observacion (descripcion_observacion, fecha_observacion, hora_observacion, id_empleado, id_detalle_presupuesto, id_detalle_venta, id_cliente)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
                current_date = timezone.localtime(timezone.now()).date()
                current_time = timezone.localtime(timezone.now()).time()
                cursor.execute(sqlInsertarObservacionPresupuesto, [descripcion_observacion, current_date, current_time, id_empleado, id_detalle_presupuesto, id_detalle_venta, id_cliente])
                idObservacion = cursor.lastrowid
                connection.commit()
                return idObservacion
        except Exception as e:
            print("Error al insertar:", str(e))
            return None

