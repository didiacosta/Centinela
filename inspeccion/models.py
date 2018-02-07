from django.db import models
from programacion.models import Programacion
# Create your models here.

class Inspeccion(models.Model):
	fechaInicio = models.DateTimeField(auto_now=True)
	longitud = models.CharField(max_length=50)
	latitud = models.CharField(max_length=50)
	programacion = models.ForeignKey(Programacion,related_name="inspeccion_programacion",on_delete=models.PROTECT)
	fechaTerminacion = models.DateTimeField()
	observacion = models.CharField(max_length=255)

	def __unicode__(self):
		return self.fecha + ' - ' + self.programacion.ordenServicio

	class Meta:			
		permissions = (
			("can_see_inspeccion","can see inspeccion"),
		)
		unique_together = [
			["programacion", "fechaInicio"],
		]