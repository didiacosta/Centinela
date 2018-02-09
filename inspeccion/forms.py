from django import forms

from .models import Inspeccion
from programacion.models import Programacion


class InspeccionForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		idPro=kwargs.pop('id')
		super(InspeccionForm, self).__init__(*args, **kwargs)

		choices=[(p.id , p.ordenServicio + ' - ' + p.fecha.strftime('%Y-%m-%d') ) for p in Programacion.objects.filter(id=idPro)]
		self.fields['programacion'].choices=choices

	class Meta:
		model = Inspeccion
		fields=('longitud','latitud','programacion','observacion')
		labels = {
			'body':'Texto'
		}
