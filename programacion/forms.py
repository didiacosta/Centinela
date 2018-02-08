from django import forms

from .models import Programacion, Municipio
from usuario.models import Usuario

class ProgramacionForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ProgramacionForm, self).__init__(*args, **kwargs)

		choices=[(u.id , u.nombres + ' ' + u.apellidos ) for u in Usuario.objects.filter(inspector=True)]
		self.fields['inspector'].choices=choices

		choicesMunicipios=[(m.id , m.nombre + ' - ' + m.departamento.nombre ) for m in Municipio.objects.all().order_by('nombre')]
		self.fields['municipio'].choices=choicesMunicipios

	class Meta:
		model = Programacion
		fields=('inspector','fecha','ordenServicio','municipio','nombreProyecto')
		labels = {
			'body':'Texto'
		}
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'class':'input-xlarge datepicker'}),
        }