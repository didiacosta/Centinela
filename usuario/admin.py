from django.contrib import admin
from .models import Usuario
# Register your models here.
class AdminUsuario(admin.ModelAdmin):
	list_display=('user','cedula','nombres','apellidos','correo','telefono')
	list_filter=('inspector','coordinador')
	search_fields=('nombres','apellidos','correo','cedula',)	

admin.site.register(Usuario,AdminUsuario)
