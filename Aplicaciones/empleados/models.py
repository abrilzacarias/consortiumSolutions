from django.db import models, connection
from django.utils import timezone

current_datetime = timezone.localtime(timezone.now())

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

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

class TipoEmpleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    descripcion_tipo_empleado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    fecha_alta_empleado = models.DateField()
    fecha_baja_empleado = models.DateField(blank=True, null=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.SET_NULL, null=True, db_column='id_tipo_empleado')  # Aquí está la corrección
    
    class Meta:
        managed = False
        db_table = 'empleado'

        
    def empleadoExiste(self, cuitl_persona):
        with connection.cursor() as cursor:
            print("Verificando existencia de CUIT:", cuitl_persona)
            cursor.execute("""
                SELECT e.id_empleado 
                FROM empleado e 
                JOIN persona p ON e.id_persona = p.id_persona
                WHERE p.cuitl_persona = %s
            """, [cuitl_persona])
            result = cursor.fetchone()
        return result is not None

    def agregarEmpleado(self, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, fecha_alta_empleado, fecha_baja_empleado, id_tipo_empleado, listaContactos):
        nombre = nombre_persona.capitalize()
        apellido = apellido_persona.capitalize()
        try:
            print("Valores recibidos:")
            print(f"nombre_persona: {nombre_persona}")
            print(f"apellido_persona: {apellido_persona}")
            print(f"cuitl_persona: {cuitl_persona}")
            print(f"direccion_persona: {direccion_persona}")
            print(f"id_tipo_empleado: {id_tipo_empleado}")
            print(f"contactos_data: {listaContactos}")
            
            # Verificar si la persona ya existe como empleado
            if not self.empleadoExiste(cuitl_persona):
                with connection.cursor() as cursor:
                    try:
                        # Insertar nueva Persona
                        cursor.execute("""
                            INSERT INTO persona (nombre_persona, apellido_persona, cuitl_persona, direccion_persona)
                            VALUES (%s, %s, %s, %s)
                        """, [nombre, apellido, cuitl_persona, direccion_persona])
                        
                        # Obtener el ID de la persona recién insertada
                        cursor.execute("SELECT LAST_INSERT_ID()")
                        idPersona = cursor.fetchone()[0]

                        print("ID de nueva persona:", idPersona)

                        # Insertar nuevo Empleado
                        cursor.execute("""
                            INSERT INTO empleado (fecha_alta_empleado, fecha_baja_empleado, id_persona, id_tipo_empleado)
                            VALUES (%s, %s, %s, %s)
                        """, [fecha_alta_empleado, fecha_baja_empleado, idPersona, id_tipo_empleado])
                        print("Nuevo empleado insertado.")

                        # Insertar contactos
                        for tipoContacto, contacto in listaContactos:
                            cursor.execute("""
                                INSERT INTO contacto (descripcion_contacto, id_tipo_contacto, id_persona)
                                VALUES (%s, %s, %s)
                            """, [contacto, tipoContacto, idPersona])
                            print("Contacto insertado:", contacto, tipoContacto)

                        connection.commit()
                        print("Transacción de inserción completada.")
                        return True

                    except Exception as e:
                        connection.rollback()
                        print("Error en la inserción de datos:", str(e))
                        return False
            else:
                print("El empleado ya existe.")
                return False
        except Exception as e:
            print("Error general:", str(e))
            return False

            
    def mostrarEmpleados(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        e.id_empleado,
                        e.fecha_alta_empleado,
                        e.fecha_baja_empleado,
                        p.id_persona,
                        p.cuitl_persona,
                        p.nombre_persona,
                        p.apellido_persona,
                        p.direccion_persona,
                        e.id_tipo_empleado,  -- Incluye el id_tipo_empleado
                        te.descripcion_tipo_empleado
                    FROM
                        empleado e
                    JOIN
                        persona p ON e.id_persona = p.id_persona
                    JOIN
                        tipo_empleado te ON e.id_tipo_empleado = te.id_tipo_empleado
                    WHERE
                        e.fecha_baja_empleado IS NULL;
                """)
                empleados = dictfetchall(cursor)

                if not empleados:
                    print("No hay empleados activos.")
                    return []

                return empleados

        except Exception as e:
            print("Error al mostrar los empleados:", str(e))
            return []


    def editarEmpleado(self, idEmpleado, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, id_tipo_empleado, contactos_data):
        try:
            print("Valores recibidos:")
            print(f"idEmpleado: {idEmpleado}")
            print(f"nombre_persona: {nombre_persona}")
            print(f"apellido_persona: {apellido_persona}")
            print(f"cuitl_persona: {cuitl_persona}")
            print(f"direccion_persona: {direccion_persona}")
            print(f"id_tipo_empleado: {id_tipo_empleado}")
            print(f"contactos_data: {contactos_data}")
            
            with connection.cursor() as cursor:
                # Obtener id_persona asociado al id_empleado
                cursor.execute("""
                    SELECT id_persona FROM empleado WHERE id_empleado = %s;
                """, [idEmpleado])
                id_persona = cursor.fetchone()[0]
                print(f"id_persona obtenido: {id_persona}")

                # Actualizar la tabla persona
                cursor.execute("""
                    UPDATE persona SET 
                        nombre_persona = %s,
                        apellido_persona = %s,
                        cuitl_persona = %s,
                        direccion_persona = %s
                    WHERE id_persona = %s;
                """, [nombre_persona, apellido_persona, cuitl_persona, direccion_persona, id_persona])
                print("Tabla persona actualizada.")

                # Actualizar la tabla empleado
                cursor.execute("""
                    UPDATE empleado SET 
                        id_tipo_empleado = %s
                    WHERE id_empleado = %s;
                """, [id_tipo_empleado, idEmpleado])
                print(f"Empleado actualizado con id_tipo_empleado: {id_tipo_empleado}")

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
                print("Empleado actualizado correctamente.")
                return True

        except Exception as e:
            print("Error al actualizar el empleado:", str(e))
            connection.rollback()
            return False




    def eliminarEmpleado(self, idEmpleado):
        try:
            with connection.cursor() as cursor:
                # Obtener id_persona asociado al id_empleado
                cursor.execute("""
                    SELECT id_persona FROM empleado WHERE id_empleado = %s;
                """, [idEmpleado])
                result = cursor.fetchone()

                if result:
                    id_persona = result[0]

                    # Actualizar la fecha de baja en la tabla empleado
                    cursor.execute("""
                        UPDATE empleado SET fecha_baja_empleado = %s WHERE id_empleado = %s;
                    """, [current_datetime, idEmpleado])

                    # Actualizar la fecha de baja en la tabla persona
                    connection.commit()
                    print("Empleado eliminado correctamente.")
                    return True
                else:
                    print("Empleado no encontrado.")
                    return False

        except Exception as e:
            print("Error al eliminar el empleado:", str(e))
            connection.rollback()
            return False

