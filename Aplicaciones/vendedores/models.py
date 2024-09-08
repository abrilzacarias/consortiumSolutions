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
    descripcion_tipo_empleado = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    fecha_alta_empleado = models.DateField()
    fecha_baja_empleado = models.DateField(blank=True, null=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    id_tipo_empleado = models.ForeignKey(TipoEmpleado, models.DO_NOTHING, db_column='id_tipo_empleado')

    class Meta:
        managed = False
        db_table = 'empleado'
        
    def vendedorExiste(self, cuitl_persona):
        with connection.cursor() as cursor:
            print("Verificando existencia de CUIT:", cuitl_persona)
            cursor.execute("""
                SELECT e.id_empleado FROM empleado e 
                JOIN persona p ON v.id_persona = p.id_persona 
                JOIN tipo_empleado te ON e.id_tipo_empleado = te.id_tipo_empleado
                WHERE p.cuitl_persona = %s 
                AND te.descripcion_tipo_empleado = 'Vendedor'
            """, [cuitl_persona])
            result = cursor.fetchone()
        return result is not None

    def agregarVendedor(self, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, fecha_alta_empleado, fecha_baja_empleado, listaContactos):
        nombre = nombre_persona.capitalize()
        apellido = apellido_persona.capitalize()
        try: 
            if not self.vendedorExiste(cuitl_persona):
                with connection.cursor() as cursor:
                    # Insertar nueva Persona
                    cursor.execute("""
                        INSERT INTO persona (nombre_persona, apellido_persona, cuitl_persona, direccion_persona)
                        VALUES (%s, %s, %s, %s) 
                    """, [nombre, apellido, cuitl_persona, direccion_persona])
                    idPersona = cursor.lastrowid

                    print("ID de nueva persona:", idPersona)

                    # Insertar nuevo Vendedor
                    #EN USUARIO QE PONGO????? y despues en tipo de empleado supongo que le pongo nomas ahora el tema de vendedores
                    cursor.execute("""
                        INSERT INTO empleado (fecha_alta_empleado, fecha_baja_empleado, id_persona)
                        VALUES (%s, %s, %s) 
                    """, [fecha_alta_empleado, fecha_baja_empleado, idPersona])
                    print("Nuevo vendedor insertado.")

                    # Insertar contactos
                    for tipoContacto, contacto in listaContactos:
                        sqlInsertarContacto = "INSERT INTO contacto (descripcion_contacto, id_tipo_contacto, id_persona) VALUES (%s, %s, %s);"
                        cursor.execute(sqlInsertarContacto, [contacto, tipoContacto, idPersona])
                        print("Contacto insertado:", contacto, tipoContacto)
                    
                    connection.commit()
                    print("Transacción de inserción completada.")
                return True
            else:
                print("El vendedor ya existe.")
                return False
        except Exception as e:
            print("Error: El vendedor ya existe en la base de datos.")
            return False

            
    def mostrarVendedor(self):
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
                    p.direccion_persona
                FROM
                    empleado e
                JOIN
                    persona p ON v.id_persona = p.id_persona
                JOIN tipo_empleado te ON e.id_tipo_empleado = te.id_tipo_empleado
                WHERE
                    v.fecha_baja_vendedor IS NULL 
                AND te.descripcion_tipo_empleado = 'Vendedor';
            """)
            vendedores = dictfetchall(cursor)
            
            return vendedores


    def editarVendedor(self, id_empleado, nombre_persona, apellido_persona, cuitl_persona, direccion_persona, contactos_data):
        with connection.cursor() as cursor:
            # Insertar nueva Persona
            cursor.execute("""
                SELECT id_persona FROM empleado WHERE id_empleado = %s;
            """, [id_empleado])
            id_persona = cursor.fetchone()[0]

            # Actualizar la tabla persona
            cursor.execute("""
                UPDATE persona SET 
                    nombre_persona = %s,
                    apellido_persona = %s,
                    cuitl_persona = %s,
                    direccion_persona = %s
                WHERE id_persona = %s;
            """, [nombre_persona, apellido_persona, cuitl_persona, direccion_persona, id_persona])

            # Actualizar o crear contactos
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


    def eliminarVendedor(self, id_empleado):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id_persona FROM empleado WHERE id_empleado = %s;
            """, [id_empleado])
            id_persona = cursor.fetchone()[0]

            cursor.execute("""
                UPDATE empleado SET fecha_baja_empleado = %s WHERE id_vendedor = %s;
            """, [current_datetime, id_empleado])

            connection.commit()

