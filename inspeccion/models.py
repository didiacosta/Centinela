from django.db import models
from programacion.models import Programacion
# Create your models here.

class Inspeccion(models.Model):
	fechaInicio = models.DateTimeField(auto_now=True)
	longitud = models.CharField(max_length=50)
	latitud = models.CharField(max_length=50)
	programacion = models.ForeignKey(Programacion,related_name="inspeccion_programacion",on_delete=models.PROTECT)
	#fechaTerminacion = models.DateTimeField()
	observacion = models.CharField(max_length=255,null=True, blank=True)

	def __unicode__(self):
		return self.fechaInicio.strftime('%Y-%m-%d %H:%M') + ' - ' + self.programacion.ordenServicio

	class Meta:			
		permissions = (
			("can_see_inspeccion","can see inspeccion"),
		)
		unique_together = [
			["programacion", "fechaInicio"],
		]

	def save(self, *args, **kwargs):
		super(Inspeccion, self).save(*args, **kwargs)
		self.programacion.cerrada=True
		self.programacion.save()