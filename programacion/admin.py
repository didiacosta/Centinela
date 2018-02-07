from django.contrib import admin
from .models import Departamento, Municipio, Programacion
# Register your models here.

class AdminDepartamento(admin.ModelAdmin):
	list_display=('nombre',)
	search_fields=('nombre',)	

admin.site.register(Departamento,AdminDepartamento)

class AdminMunicipio(admin.ModelAdmin):
	list_display=('departamento','nombre',)
	list_filter=('departamento',)
	search_fields=('nombre',)	

admin.site.register(Municipio,AdminMunicipio)

class AdminProgramacion(admin.ModelAdmin):
	list_display=('inspector','fecha','ordenServicio','municipio','nombreProyecto','cerrada',)
	list_filter=('inspector','cerrada',)
	search_fields=('inspector','ordenServicio','nombreProyecto',)	

admin.site.register(Programacion,AdminProgramacion)



