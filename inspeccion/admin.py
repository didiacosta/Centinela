from django.contrib import admin
from .models import Inspeccion
# Register your models here.

class AdminInspeccion(admin.ModelAdmin):
	list_display=('longitud','latitud','programacion','observacion',)
	list_filter=('fechaInicio',)	

admin.site.register(Inspeccion,AdminInspeccion)

