from django.db import models
from django.db import connection
from ..login.models import MyUser
class Actividades(): 
    def listarActividades(self):
        with connection.cursor() as cursor:
            sql_listar_actividades = """
                SELECT 
                    ROW_NUMBER() OVER (ORDER BY fecha_actividad DESC) AS actividad_id,
                    tipo_actividad,
                    descripcion,
                    fecha_actividad
                FROM (
                    -- Alta vendedor
                    SELECT 
                        'Alta vendedor' AS tipo_actividad,
                        CONCAT('Vendedor agregado: ', p.nombre_persona) AS descripcion,
                        e.fecha_alta_empleado AS fecha_actividad
                    FROM 
                        empleado e 
                    JOIN 
                        persona p ON p.id_persona = e.id_persona
                    JOIN 
                        tipo_empleado te ON te.id_tipo_empleado = e.id_tipo_empleado
                    WHERE 
                        te.descripcion_tipo_empleado = 'Vendedor'
                        AND e.fecha_alta_empleado IS NOT NULL

                    UNION ALL

                    -- Baja vendedor
                    SELECT 
                        'Baja vendedor' AS tipo_actividad,
                        CONCAT('Vendedor dado de baja: ', p.nombre_persona) AS descripcion,
                        e.fecha_baja_empleado AS fecha_actividad
                    FROM 
                        empleado e 
                    JOIN 
                        persona p ON p.id_persona = e.id_persona
                    JOIN 
                        tipo_empleado te ON te.id_tipo_empleado = e.id_tipo_empleado
                    WHERE 
                        te.descripcion_tipo_empleado = 'Vendedor'
                        AND e.fecha_baja_empleado IS NOT NULL

                    UNION ALL

                    -- Baja cliente
                    SELECT 
                        'Baja cliente' AS tipo_actividad,
                        CONCAT('Cliente dado de baja: ', p.nombre_persona) AS descripcion,
                        c.fecha_baja_cliente AS fecha_actividad
                    FROM 
                        cliente c 
                    JOIN 
                        persona p ON p.id_persona = c.id_persona
                    WHERE 
                        c.fecha_baja_cliente IS NOT NULL
                    
                        UNION ALL

                    -- Alta cliente
                    SELECT 
                        'Alta cliente' AS tipo_actividad,
                        CONCAT('Cliente dado de alta: ', p.nombre_persona) AS descripcion,
                        c.fecha_alta_cliente AS fecha_actividad
                    FROM 
                        cliente c 
                    JOIN 
                        persona p ON p.id_persona = c.id_persona
                    WHERE 
                        c.fecha_alta_cliente IS NOT NULL

                    UNION ALL

                    -- Observación
                    SELECT 
                        'Observacion' AS tipo_actividad,
                        descripcion_observacion AS descripcion,
                        fecha_observacion AS fecha_actividad
                    FROM 
                        observacion
                ) AS actividades
                ORDER BY 
                    fecha_actividad DESC;
            """
            cursor.execute(sql_listar_actividades)
            actividades = cursor.fetchall()

        return actividades

    

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_usuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'administrador'


class ArchivoPersonal(models.Model):
    id_archivo_personal = models.AutoField(primary_key=True)
    documento_archivo_personal = models.CharField(max_length=200)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'archivo_personal'


class ArchivoVenta(models.Model):
    id_archivo_venta = models.AutoField(primary_key=True)
    documento_archivo_venta = models.CharField(max_length=200)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')

    class Meta:
        managed = False
        db_table = 'archivo_venta'


class CategoriaServicio(models.Model):
    id_categoria_servicio = models.AutoField(primary_key=True)
    nombre_categoria_servicio = models.CharField(max_length=60)

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


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    clave_afgip_cliente = models.CharField(max_length=11, blank=True, null=True)
    conversion_cliente = models.IntegerField()
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_matricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    descripcion_contacto = models.CharField(max_length=100)
    id_tipo_contacto = models.ForeignKey('TipoContacto', models.DO_NOTHING, db_column='id_tipo_contacto')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'contacto'


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_alta_contrato = models.DateField()
    fecha_baja_contrato = models.DateField(blank=True, null=True)
    horas_trabajadas = models.IntegerField()
    salario_empleado = models.DecimalField(max_digits=10, decimal_places=0)
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')
    id_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_administrador')

    class Meta:
        managed = False
        db_table = 'contrato'


class Designacion(models.Model):
    id_designacion = models.AutoField(primary_key=True)
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    fecha_alta_designacion = models.DateField()
    fecha_baja_designacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designacion'


class DetallePresupuesto(models.Model):
    id_detalle_presupuesto = models.AutoField(primary_key=True)
    cantidad_detalle_presupuesto = models.IntegerField()
    precio_unitario_detalle_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    precio_total_datalle_preventa = models.DecimalField(max_digits=10, decimal_places=0)
    id_presupuesto = models.ForeignKey('Presupuesto', models.DO_NOTHING, db_column='id_presupuesto')
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'detalle_presupuesto'


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    cantidad_detalle_venta = models.IntegerField()
    precio_unitario_detalle_venta = models.DecimalField(max_digits=10, decimal_places=0)
    precio_total_detalle_venta = models.DecimalField(max_digits=10, decimal_places=0)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta')
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Edificio(models.Model):
    id_edificio = models.AutoField(primary_key=True)
    nombre_edificio = models.CharField(max_length=70)
    direccion_edificio = models.CharField(max_length=70)
    cuit_edificio = models.CharField(max_length=11)
    id_tipo_edificio = models.ForeignKey('TipoEdificio', models.DO_NOTHING, db_column='id_tipo_edificio')
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'edificio'


class EstadoVenta(models.Model):
    id_estado_venta = models.AutoField(primary_key=True)
    descripcion_estado_venta = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'estado_venta'


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    numero_matricula = models.CharField(max_length=70)
    vencimiento_matricula = models.DateField()

    class Meta:
        managed = False
        db_table = 'matricula'


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class Observacion(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    descripcion_observacion = models.CharField(max_length=2000)
    fecha_hora_observacion = models.DateTimeField()
    id_detalle_presupuesto = models.ForeignKey(DetallePresupuesto, models.DO_NOTHING, db_column='id_detalle_presupuesto', blank=True, null=True)
    id_detalle_venta = models.ForeignKey(DetalleVenta, models.DO_NOTHING, db_column='id_detalle_venta', blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observacion'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    cuitl_persona = models.CharField(max_length=11, blank=True, null=True)
    nombre_persona = models.CharField(max_length=70)
    apellido_persona = models.CharField(max_length=70)
    direccion_persona = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'persona'


class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    fecha_hora_presupuesto = models.DateTimeField()
    monto_total_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')
    id_edificio = models.ForeignKey(Edificio, models.DO_NOTHING, db_column='id_edificio')

    class Meta:
        managed = False
        db_table = 'presupuesto'


class RegistroEstadoVenta(models.Model):
    id_registro_estado_venta = models.AutoField(primary_key=True)
    fecha_hora_registro_estado_venta = models.DateTimeField()
    id_detalle_venta = models.ForeignKey(DetalleVenta, models.DO_NOTHING, db_column='id_detalle_venta')
    id_estado_venta = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado_venta')
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor')

    class Meta:
        managed = False
        db_table = 'registro_estado_venta'


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=70)
    requiere_pago_servicio = models.IntegerField()
    precio_base_servicio = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    id_categoria_servicio = models.ForeignKey(CategoriaServicio, models.DO_NOTHING, db_column='id_categoria_servicio')

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoContacto(models.Model):
    id_tipo_contacto = models.AutoField(primary_key=True)
    descripcion_tipo_contacto = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'tipo_contacto'


class TipoEdificio(models.Model):
    id_tipo_edificio = models.AutoField(primary_key=True)
    nombre_tipo_edificio = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_edificio'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    clave_usuario = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuario'


class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    fecha_alta_vendedor = models.DateField()
    fecha_baja_vendedor = models.DateField(blank=True, null=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_usuario = models.ForeignKey(MyUser, models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'vendedor'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_hora_venta = models.DateTimeField()
    monto_total_venta = models.DecimalField(max_digits=10, decimal_places=0)
    id_edificio = models.ForeignKey(Edificio, models.DO_NOTHING, db_column='id_edificio')
    id_vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING, db_column='id_vendedor')
    id_metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='id_metodo_pago')

    class Meta:
        managed = False
        db_table = 'venta'
