from django.db import models
from django.conf import settings
# Create your models here.

class Usuario(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	cedula = models.BigIntegerField(unique=True)
	nombres = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	correo = models.EmailField(max_length=70,blank=True, null=True)
	telefono = models.CharField(max_length=200,blank=True, null=True)
	inspector = models.BooleanField(default=True)
	coordinador = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.username	
