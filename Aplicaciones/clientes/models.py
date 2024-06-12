from django.db import models
from django.db import connection
from django.utils import timezone


from django.utils import timezone


# Obtener la fecha y hora actual en la zona horaria local
current_datetime = timezone.localtime(timezone.now())

# Imprimir la fecha y hora actual en formato de fecha y hora


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

class Clientes():
    def listarClientes(self):
        with connection.cursor() as cursor:
            sqlListarClientes = """
                    SELECT * FROM vista_detallada_clientes;
                    """
            cursor.execute(sqlListarClientes)
            # Guardar en la variable resultados todos los resultados devueltos por la consulta.
            resultados = cursor.fetchall()
        return resultados
    
    def agregarCliente(self, nombre_cliente, apellido_cliente, cuitl_cliente, direccion_cliente, clave_afgip_cliente, tipo_cliente, numero_matricula, vencimiento_matricula, lista_contactos, vendedor_asignado=None):
        nombre = nombre_cliente.capitalize()
        apellido = apellido_cliente.capitalize()
        try:
            # Verificar si el cliente ya existe
            if self.clienteExiste(cuitl_cliente):
                print("El cliente ya existe en la base de datos.")
                return None
            with connection.cursor() as cursor:
                sqlInsertarPersona = "INSERT INTO persona (nombre_persona, apellido_persona, cuitl_persona, direccion_persona) VALUES (%s, %s, %s, %s);"
                cursor.execute(sqlInsertarPersona, [nombre, apellido, cuitl_cliente, direccion_cliente])
                idPersona = cursor.lastrowid  # Esto obtiene el ID en la mayoría de las bases de datos
                connection.commit()

                sqlInsertarMatricula = "INSERT INTO matricula (numero_matricula, vencimiento_matricula) VALUES (%s, %s);"
                cursor.execute(sqlInsertarMatricula, [numero_matricula, vencimiento_matricula])
                idMatricula = cursor.lastrowid  # Esto obtiene el ID en la mayoría de las bases de datos
                connection.commit()

                sqlInsertarCliente = "INSERT INTO cliente (clave_afgip_cliente, conversion_cliente, id_persona, id_matricula) VALUES (%s, %s, %s, %s);"
                cursor.execute(sqlInsertarCliente, [clave_afgip_cliente, tipo_cliente, idPersona, idMatricula])
                idCliente = cursor.lastrowid  # Esto obtiene el ID en la mayoría de las bases de datos
                connection.commit()

                for tipo_contacto, contacto in lista_contactos:
                    sqlInsertarContacto = "INSERT INTO contacto (descripcion_contacto, id_tipo_contacto, id_persona) VALUES (%s, %s, %s);"
                    cursor.execute(sqlInsertarContacto, [contacto, tipo_contacto, idPersona])
                    connection.commit()
                # Verificar si el vendedor actual es nulo para permitir la edición del vendedor asignado
                if vendedor_asignado == '':
                    vendedor_asignado = None
                    
                if vendedor_asignado is not None:
                    # Llama al método agregarDesignacionVendedor con los IDs del vendedor y el cliente
                    if self.agregarDesignacionVendedor(vendedor_asignado, idCliente):
                        print("Designación de vendedor agregada exitosamente.")
                    else:
                        print("Hubo un error al agregar la designación de vendedor.")

                return idCliente
        except Exception as e:
            print("Error al insertar:", str(e))
            return None

        
    def editarCliente(self, id_cliente, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, clave_afgip_cliente, tipo_cliente, matricula_cliente, vencimiento_matricula, contactos_data):
        with connection.cursor() as cursor:
            # Obtener el id_persona relacionado con el id_cliente
            cursor.execute("""
                SELECT id_persona, id_matricula FROM cliente WHERE id_cliente = %s;
            """, [id_cliente])
            cliente_row = cursor.fetchone()
            if cliente_row is None:
                raise ValueError("No se encontró un cliente con el id_cliente proporcionado.")
            id_persona, id_matricula = cliente_row

            # Actualizar la tabla persona
            cursor.execute("""
                UPDATE persona SET 
                    nombre_persona = %s,
                    apellido_persona = %s,
                    cuitl_persona = %s,
                    direccion_persona = %s
                WHERE id_persona = %s;
            """, [nombre_persona, apellido_persona, cuitl_persona, direccion_persona, id_persona])

            # Actualizar la tabla matricula
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

            # Actualizar los contactos del cliente
            for contacto_data in contactos_data:
                contacto_id = contacto_data.get('id_contacto')
                tipo_contacto_id = contacto_data.get('tipo_contacto_id')
                descripcion_contacto = contacto_data.get('descripcion_contacto')

                if contacto_id:  # Si el contacto ya existe, actualizarlo
                    cursor.execute("""
                        UPDATE contacto SET 
                            descripcion_contacto = %s,
                            id_tipo_contacto = %s
                        WHERE id_contacto = %s;
                    """, [descripcion_contacto, tipo_contacto_id, contacto_id])
                else:  # Si el contacto es nuevo, crearlo
                    cursor.execute("""
                        INSERT INTO contacto (descripcion_contacto, id_tipo_contacto, id_persona) 
                        VALUES (%s, %s, %s);
                    """, [descripcion_contacto, tipo_contacto_id, id_persona])

            # Guardar los cambios en la base de datos
            connection.commit()

            # Retornar True si la edición fue exitosa
            return True
        
    def eliminarCliente(self, id_cliente):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id_persona FROM cliente WHERE id_cliente = %s;
            """, [id_cliente])
            id_persona = cursor.fetchone()[0]

            cursor.execute("DELETE FROM edificio WHERE id_cliente = %s;", [id_cliente])
            # Eliminar el vendedor de la tabla 'vendedor'
            cursor.execute("DELETE FROM cliente WHERE id_cliente = %s;", [id_cliente])
            cursor.execute("DELETE FROM contacto WHERE id_persona = %s;", [id_persona])
            # Ahora que el vendedor ha sido eliminado, podemos eliminar la persona asociada
            cursor.execute("DELETE FROM persona WHERE id_persona = %s;", [id_persona])
    
    def agregarEdificio(self, nombre_edificio, direccion_edificio, cuit_edificio, tipo_edificio, id_cliente):
        try:
            with connection.cursor() as cursor:
                sqlInsertarEdificio = "INSERT INTO edificio (nombre_edificio, direccion_edificio, cuit_edificio, id_tipo_edificio, id_cliente) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sqlInsertarEdificio, [nombre_edificio, direccion_edificio, cuit_edificio, tipo_edificio, id_cliente])
                idEdificio = cursor.lastrowid  # Esto obtiene el ID en la mayoría de las bases de datos
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
        
    def agregarDesignacionVendedor(self, id_vendedor, id_cliente):
        try:
            with connection.cursor() as cursor:
                # Define la consulta SQL para insertar una nueva designación de vendedor
                sql_insert = """
                    INSERT INTO designacion (id_vendedor, id_cliente, fecha_alta_designacion)
                    VALUES (%s, %s, %s)
                """
                # Ejecuta la consulta SQL con los parámetros proporcionados
                cursor.execute(sql_insert, [id_vendedor, id_cliente, current_datetime])
                # Guarda los cambios en la base de datos
                connection.commit()
                # Retorna True si la inserción fue exitosa
                return True
        except Exception as e:
            # En caso de error, imprime el mensaje de error y retorna False
            print("Error al insertar designación de vendedor:", str(e))
            return False
        
    def eliminarDesignacionVendedor(self, id_cliente, id_vendedor):
        try:
            with connection.cursor() as cursor:
                # Actualizar la tabla designacion para establecer la fecha de baja
                cursor.execute("""
                    UPDATE designacion 
                    SET fecha_baja_designacion = %s 
                    WHERE id_cliente = %s AND id_vendedor = %s AND fecha_baja_designacion IS NULL;
                """, [current_datetime, id_cliente, id_vendedor])

                # Guardar los cambios en la base de datos
                connection.commit()
                return True
        except Exception as e:
            print("Error al eliminar designación de vendedor:", str(e))
            return False

    def agregarObservacion(self, id_cliente, descripcion_observacion):
        try:
            with connection.cursor() as cursor:
                sqlInsertarObservacionCliente = "INSERT INTO observacion (descripcion_observacion, fecha_hora_observacion, id_cliente, id_detalle_presupuesto, id_detalle_venta) VALUES (%s, %s, %s, NULL, NULL);"
                cursor.execute(sqlInsertarObservacionCliente, [descripcion_observacion, current_datetime, id_cliente])
                idObservacion = cursor.lastrowid  # Esto obtiene el ID en la mayoría de las bases de datos
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

                print(f"Datos del cliente antes de formatear contactos: {cliente}")  # Agregar impresión para depuración

                # Guardar los valores de vendedor antes de formatear los contactos
                vendedor_asignado = cliente.get('vendedor_asignado')
                id_vendedor_asignado = cliente.get('id_vendedor_asignado')

                # Obtener los contactos del cliente desde el modelo Contacto
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

                print(f"Datos del cliente después de formatear contactos: {cliente}")  # Agregar impresión para depuración

            return cliente

    def clienteExiste(self, cuit):
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_persona FROM persona WHERE cuitl_persona = %s", [cuit])
                result = cursor.fetchone()
            return result is not None