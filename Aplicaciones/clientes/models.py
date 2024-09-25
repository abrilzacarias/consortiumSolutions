from django.db import models
from django.db import connection
from django.utils import timezone
from datetime import datetime


# Obtener la fecha y hora actual en la zona horaria local
current_datetime = timezone.localtime(timezone.now())

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    cuitl_persona = models.CharField(max_length=11, blank=True, null=True)
    nombre_persona = models.CharField(max_length=70)
    apellido_persona = models.CharField(max_length=70)
    direccion_persona = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'persona'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=45)
    clave_usuario = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuario'

class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    descripcion_contacto = models.CharField(max_length=100)
    id_tipo_contacto = models.ForeignKey('TipoContacto', models.DO_NOTHING, db_column='id_tipo_contacto')
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'contacto'

class TipoContacto(models.Model):
    id_tipo_contacto = models.AutoField(primary_key=True)
    descripcion_tipo_contacto = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'tipo_contacto'

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    clave_afgip_cliente = models.CharField(max_length=11, blank=True, null=True)
    conversion_cliente = models.IntegerField()
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_matricula = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='id_matricula', blank=True, null=True)
    id_empleado = models.ForeignKey('empleados.Empleado', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cliente'


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    numero_matricula = models.CharField(max_length=70)
    vencimiento_matricula = models.DateField()

    class Meta:
        managed = False
        db_table = 'matricula'
        
class Clientes():
    
    def listarClientes(self):
        with connection.cursor() as cursor:
            sqlListarClientes = """
                    SELECT * FROM vista_detallada_clientes;
                    """
            cursor.execute(sqlListarClientes)
            resultados = cursor.fetchall()
        return resultados
    
    def agregarCliente(self, nombre_cliente, apellido_cliente, cuitl_cliente, direccion_cliente, clave_afgip_cliente, tipo_cliente, numero_matricula, vencimiento_matricula, lista_contactos, empleado_asignado=None):
        nombre = nombre_cliente.capitalize()
        apellido = apellido_cliente.capitalize()
        if empleado_asignado == '':
            empleado_asignado = None

        try:
            # Verificar si el cliente ya existe
            if self.clienteExiste(cuitl_cliente):
                print("El cliente ya existe en la base de datos.")
                return None
            with connection.cursor() as cursor:
                sqlInsertarPersona = "INSERT INTO persona (nombre_persona, apellido_persona, cuitl_persona, direccion_persona) VALUES (%s, %s, %s, %s);"
                cursor.execute(sqlInsertarPersona, [nombre, apellido, cuitl_cliente, direccion_cliente])
                idPersona = cursor.lastrowid  
                connection.commit()

                sqlInsertarMatricula = "INSERT INTO matricula (numero_matricula, vencimiento_matricula) VALUES (%s, %s);"
                cursor.execute(sqlInsertarMatricula, [numero_matricula, vencimiento_matricula])
                idMatricula = cursor.lastrowid  
                connection.commit()

                sqlInsertarCliente = "INSERT INTO cliente (clave_afgip_cliente, conversion_cliente, id_persona, id_matricula) VALUES (%s, %s, %s, %s);"
                cursor.execute(sqlInsertarCliente, [clave_afgip_cliente, tipo_cliente, idPersona, idMatricula])
                idCliente = cursor.lastrowid  
                connection.commit()

                for tipo_contacto, contacto in lista_contactos:
                    sqlInsertarContacto = "INSERT INTO contacto (descripcion_contacto, id_tipo_contacto, id_persona) VALUES (%s, %s, %s);"
                    cursor.execute(sqlInsertarContacto, [contacto, tipo_contacto, idPersona])
                    connection.commit()
                # Verificar si el vendedor actual es nulo para permitir la edición del vendedor asignado
                if empleado_asignado == '':
                    empleado_asignado = None
                    
                if empleado_asignado is not None:
                    if self.agregarDesignacionVendedor(empleado_asignado, idCliente):
                        print("Designación de vendedor agregada exitosamente.")
                    else:
                        print("Hubo un error al agregar la designación de vendedor.")

                return idCliente
        except Exception as e:
            print("Error al insertar:", str(e))
            return None

        
    def editarCliente(self, id_cliente, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, clave_afgip_cliente, tipo_cliente, matricula_cliente, vencimiento_matricula, contactos_data):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id_persona, id_matricula FROM cliente WHERE id_cliente = %s;
            """, [id_cliente])
            cliente_row = cursor.fetchone()
            if cliente_row is None:
                raise ValueError("No se encontró un cliente con el id_cliente proporcionado.")
            id_persona, id_matricula = cliente_row

            cursor.execute("""
                UPDATE persona SET 
                    nombre_persona = %s,
                    apellido_persona = %s,
                    cuitl_persona = %s,
                    direccion_persona = %s
                WHERE id_persona = %s;
            """, [nombre_persona, apellido_persona, cuitl_persona, direccion_persona, id_persona])

            cursor.execute("""
                UPDATE matricula SET 
                    numero_matricula = %s,
                    vencimiento_matricula = %s
                WHERE id_matricula = %s;
            """, [matricula_cliente, vencimiento_matricula, id_matricula])

            cursor.execute("""
                UPDATE cliente SET
                    clave_afgip_cliente = %s,
                    conversion_cliente = %s 
                WHERE id_cliente = %s;
            """, [clave_afgip_cliente, tipo_cliente, id_cliente])

            # Actualizar o crear contactos
            for contacto_data in contactos_data:
                contacto_id = contacto_data.get('id_contacto')
                tipo_contacto_id = contacto_data.get('tipo_contacto_id')
                descripcion_contacto = contacto_data.get('descripcion_contacto')

                print(f"Procesando contacto: {contacto_data}")
                
                if contacto_id.isdigit():  # Verifica que el contacto_id sea un número válido
                    cursor.execute("""
                        UPDATE contacto SET 
                            descripcion_contacto = %s,
                            id_tipo_contacto = %s
                        WHERE id_contacto = %s;
                    """, [descripcion_contacto, tipo_contacto_id, contacto_id])
                    print(f"Contacto actualizado con id: {contacto_id}")
                else:  # Si el contacto es nuevo, crearlo
                    cursor.execute("""
                        INSERT INTO contacto (descripcion_contacto, id_tipo_contacto, id_persona) 
                        VALUES (%s, %s, %s);
                    """, [descripcion_contacto, tipo_contacto_id, id_persona])
                    print("Nuevo contacto creado.")

            connection.commit()

            return True
        
    def eliminarCliente(self, id_cliente):
        with connection.cursor() as cursor:
            # Actualiza la fecha de baja del cliente en lugar de eliminar
            cursor.execute("""
                UPDATE cliente
                SET fecha_baja_cliente = %s
                WHERE id_cliente = %s;
            
        """, [current_datetime, id_cliente])
            
    def agregarEdificio(self, nombre_edificio, direccion_edificio, cuit_edificio, tipo_edificio, id_cliente):
        try:
            with connection.cursor() as cursor:
                sqlInsertarEdificio = "INSERT INTO edificio (nombre_edificio, direccion_edificio, cuit_edificio, id_tipo_edificio, id_cliente) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sqlInsertarEdificio, [nombre_edificio, direccion_edificio, cuit_edificio, tipo_edificio, id_cliente])
                idEdificio = cursor.lastrowid  
                connection.commit()

                return idEdificio
        except Exception as e:
            print("Error al insertar:", str(e))
            return None
        
    def obtenerIdPersona(self, idCliente):
        with connection.cursor() as cursor:
            # Obtener el id_persona relacionado con el id_cliente
            cursor.execute("""
                SELECT id_persona FROM cliente WHERE id_cliente = %s;
            """, [idCliente])
            idpersona = cursor.fetchone()
            if idpersona is None:
                raise ValueError("No se encontró un cliente con el id_cliente proporcionado.")
            return idpersona
        
        
    def agregarDesignacionVendedor(self, id_empleado, id_cliente):
        cursor = connection.cursor()
        try:
            # Verificar si ya existe una designación activa para este cliente
            cursor.execute("""
                SELECT id_designacion, id_empleado FROM designacion 
                WHERE id_cliente = %s AND fecha_baja_designacion IS NULL
            """, [id_cliente])
            designacion_existente = cursor.fetchone()

            if designacion_existente:
                id_designacion, id_empleado_actual = designacion_existente
                if id_empleado_actual != id_empleado:
                    # Si existe una designación activa pero con un empleado diferente,
                    # actualizamos el empleado y la fecha de alta
                    cursor.execute("""
                        UPDATE designacion 
                        SET id_empleado = %s, fecha_alta_designacion = %s
                        WHERE id_designacion = %s
                    """, [id_empleado, timezone.now().date(), id_designacion])
                else:
                    # Si el empleado es el mismo, no hacemos nada
                    return True
            else:
                # Si no existe una designación activa, creamos una nueva
                id_administrador = 1  # Este valor debe ser adecuado según tu contexto
                fecha_alta_designacion = timezone.now().date()

                cursor.execute("""
                    INSERT INTO designacion (id_empleado, id_cliente, fecha_alta_designacion, id_administrador)
                    VALUES (%s, %s, %s, %s)
                """, [id_empleado, id_cliente, fecha_alta_designacion, id_administrador])
            
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al manejar designación de vendedor: {e}")
            connection.rollback()
            return False

        
    def agregarObservacion(self, id_cliente, descripcion_observacion):
        try:
            with connection.cursor() as cursor:
                sqlInsertarObservacionCliente = "INSERT INTO observacion (descripcion_observacion, fecha_hora_observacion, id_cliente, id_detalle_presupuesto, id_detalle_venta) VALUES (%s, %s, %s, NULL, NULL);"
                cursor.execute(sqlInsertarObservacionCliente, [descripcion_observacion, current_datetime, id_cliente])
                idObservacion = cursor.lastrowid  
                connection.commit()
                return idObservacion
        except Exception as e:
            print("Error al insertar:", str(e))
            return None
        
    def obtenerClientePorId(self, id_cliente):
        with connection.cursor() as cursor:
            sqlObtenerCliente = """
                SELECT * FROM vista_detallada_clientes WHERE id_cliente = %s;
            """
            cursor.execute(sqlObtenerCliente, [id_cliente])
            row = cursor.fetchone()

            if row:
                idpersona = self.obtenerIdPersona(id_cliente)
                columns = [col[0] for col in cursor.description]
                cliente = dict(zip(columns, row))

                #print(f"Datos del cliente antes de formatear contactos: {cliente}")  

                vendedor_asignado = cliente.get('vendedor_asignado')
                id_vendedor_asignado = cliente.get('id_vendedor_asignado')

                contactos = Contacto.objects.filter(id_persona=idpersona)

                # Formatear los contactos en un diccionario
                cliente['contactos'] = [
                    {
                        'id_contacto': contacto.id_contacto,
                        'tipo_contacto': contacto.id_tipo_contacto.descripcion_tipo_contacto,
                        'tipo_contacto_id': contacto.id_tipo_contacto.id_tipo_contacto,
                        'descripcion_contacto': contacto.descripcion_contacto
                    }
                    for contacto in contactos
                ]

                # Restaurar los valores de vendedor
                cliente['vendedor_asignado'] = vendedor_asignado
                cliente['id_vendedor_asignado'] = id_vendedor_asignado

            return cliente

    def clienteExiste(self, cuit):
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_persona FROM persona WHERE cuitl_persona = %s", [cuit])
                result = cursor.fetchone()
            return result is not None
    
   
    def eliminarEdificio(cls, id_edificio):
         print('HOLAAAAAAAA')
         print(f'edificio model {id_edificio}')
         with connection.cursor() as cursor:
            # Actualiza la fecha de baja del edificio en lugar de eliminar
            cursor.execute("""
                UPDATE edificio
                SET fecha_baja_edificio = %s
                WHERE id_edificio = %s;
            
        """, [current_datetime, id_edificio])
            connection.commit()

    
class TipoEdificio(models.Model):
    id_tipo_edificio = models.AutoField(primary_key=True)
    nombre_tipo_edificio = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_edificio'

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