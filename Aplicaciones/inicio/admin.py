from django.contrib import admin
from .models import Administrador, ArchivoPersonal, ArchivoVenta, CategoriaServicio, Cliente, \
                    Contacto, Contrato, Designacion, DetallePresupuesto, DetalleVenta, \
                    Edificio, EstadoVenta, Matricula, MetodoPago, Observacion, Persona, \
                    Presupuesto, RegistroEstadoVenta, Servicio, TipoContacto, TipoEdificio, Vendedor, Venta

# Registro de todos los modelos
admin.site.register(Administrador)
admin.site.register(ArchivoPersonal)
admin.site.register(ArchivoVenta)
admin.site.register(CategoriaServicio)
admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Contrato)
admin.site.register(Designacion)
admin.site.register(DetallePresupuesto)
admin.site.register(DetalleVenta)
admin.site.register(Edificio)
admin.site.register(EstadoVenta)
admin.site.register(Matricula)
admin.site.register(MetodoPago)
admin.site.register(Observacion)
admin.site.register(Persona)
admin.site.register(Presupuesto)
admin.site.register(RegistroEstadoVenta)
admin.site.register(Servicio)
admin.site.register(TipoContacto)
admin.site.register(TipoEdificio)
admin.site.register(Vendedor)
admin.site.register(Venta)
