from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Rol)
admin.site.register(PersonalSalud)
admin.site.register(Horas)
admin.site.register(Ficha)
admin.site.register(Cita)
admin.site.register(DatosAtencion)
admin.site.register(Antecedentes)