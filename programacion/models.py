from django.db import models
from usuario.models import Usuario
# Create your models here.

class Departamento(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class Municipio(models.Model):
	departamento = models.ForeignKey(Departamento,related_name="departamento_municipio",on_delete=models.PROTECT)
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre + ' - ' + self.departamento.nombre 

class Programacion(models.Model):
	inspector = models.ForeignKey(Usuario,related_name="programacion_usuario",on_delete=models.PROTECT)
	fecha = models.DateTimeField()
	ordenServicio = models.CharField(max_length=25)
	municipio = models.ForeignKey(Municipio,related_name="programacion_municipio",on_delete=models.PROTECT)
	nombreProyecto = models.CharField(max_length=255)
	cerrada = models.BooleanField(default=False)

	def __unicode__(self):
		return self.inspector.user.username + ' - ' + self.fecha.strftime('%Y-%m-%d %H:%M')
	
	class Meta:			
		permissions = (
			("can_see_programacion","can see programacion"),
		)
		unique_together = [
			["inspector", "fecha"],
		]