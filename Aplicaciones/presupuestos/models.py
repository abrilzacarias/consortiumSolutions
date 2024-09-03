from django.db import models
from django.db import connection
from django.utils import timezone


current_datetime = timezone.localtime(timezone.now())

from django.db import models

class Presupuesto(models.Model):
    id_presupuesto = models.AutoField(primary_key=True)
    fecha_hora_presupuesto = models.DateTimeField()
    monto_total_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    id_vendedor = models.IntegerField() 
    id_edificio = models.IntegerField()

    class Meta:
        db_table = 'presupuesto'
        managed = False  # Esto indica que Django no debería gestionar la creación de la tabla

class DetallePresupuesto(models.Model):
    id_detalle_presupuesto = models.AutoField(primary_key=True)
    cantidad_detalle_presupuesto = models.IntegerField()
    precio_unitario_detalle_presupuesto = models.DecimalField(max_digits=10, decimal_places=0)
    precio_total_datalle_preventa = models.DecimalField(max_digits=10, decimal_places=0)
    id_presupuesto = models.ForeignKey('Presupuesto', models.DO_NOTHING, db_column='id_persona')
    id_servicio = models.IntegerField()

    class Meta:
        db_table = 'detalle_presupuesto'
        managed = False  # Esto indica que Django no debería gestionar la creación de la tabla