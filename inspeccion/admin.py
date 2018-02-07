from django.contrib import admin
from .models import Inspeccion
# Register your models here.

class AdminInspeccion(admin.ModelAdmin):
	list_display=('fechaInicio','longitud','latitud','programacion','fechaTerminacion','observacion',)
	list_filter=('fechaInicio',)	

admin.site.register(Inspeccion,AdminInspeccion)

