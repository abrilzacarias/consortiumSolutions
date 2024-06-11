from django.db import models
from django.db import connection
# Create your models here.
class Actividades(): 
    def listarActividades(self):
        with connection.cursor() as cursor:
            sqlListarActividades = """
                    SELECT 
                    ROW_NUMBER() OVER (ORDER BY fecha_actividad DESC) AS actividad_id,
                    tipo_actividad,
                    descripcion,
                    fecha_actividad
                FROM (
                    SELECT 
                        'Alta vendedor' AS tipo_actividad,
                        CONCAT('Vendedor agregado: ', p.nombre_persona) AS descripcion,
                        v.fecha_alta_vendedor AS fecha_actividad
                    FROM 
                        vendedor v JOIN persona p ON p.id_persona = v.id_persona
                    WHERE 
                        v.fecha_alta_vendedor IS NOT NULL

                    UNION ALL

                    SELECT 
                        'Baja vendedor' AS tipo_actividad,
                        CONCAT('Vendedor dado de baja: ', p.nombre_persona) AS descripcion,
                        v.fecha_baja_vendedor AS fecha_actividad
                    FROM 
                        vendedor v JOIN persona p ON p.id_persona = v.id_persona
                    WHERE 
                        v.fecha_baja_vendedor IS NOT NULL

                    UNION ALL

                    SELECT 
                        'Baja cliente' AS tipo_actividad,
                        CONCAT('Cliente dado de baja: ', p.nombre_persona) AS descripcion,
                        c.fecha_baja_cliente AS fecha_actividad
                    FROM 
                        cliente c JOIN persona p ON p.id_persona = c.id_persona
                    WHERE 
                        c.fecha_baja_cliente IS NOT NULL

                    UNION ALL

                    SELECT 
                        'Observacion' AS tipo_actividad,
                        descripcion_observacion AS descripcion,
                        fecha_hora_observacion AS fecha_actividad
                    FROM 
                        observacion
                ) AS actividades
                ORDER BY 
                    fecha_actividad DESC;
                    """
            cursor.execute(sqlListarActividades)
            # Guardar en la variable resultados todos los resultados devueltos por la consulta.
            actividades = cursor.fetchall()

        return actividades