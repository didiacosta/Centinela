from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Programacion
from usuario.models import Usuario

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings

from .forms import ProgramacionForm
from django.db.models import Q
# Create your views here.

class ProgramacionListView(ListView):
	model=Programacion
	template_name = 'programacion/programacion-list.html'
	paginate_by = 10


	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		query = self.request.GET.get('q', '')
		inspector = self.request.GET.get('cmbInspectores', '')
		ejecutada = self.request.GET.get('cmbEjecutada', '')

		qset=(~Q(id=0))

		if query:
			qset=qset & (Q(ordenServicio__icontains=query) | Q(nombreProyecto__icontains=query))
		if usuario.coordinador==False:
			qset = qset & (Q(inspector=usuario))
		else:
			if inspector and inspector !='0':
				objInspector = Usuario.objects.get(pk=inspector)
				if objInspector:
					qset=qset & (Q(inspector=objInspector))
		if ejecutada:
			if ejecutada=='1':
				qset=qset & Q(cerrada=False)
			elif ejecutada=='2':
				qset=qset & Q(cerrada=True)
		
		queryset= self.model.objects.filter(qset).order_by('-fecha')

		return queryset

	def get_context_data(self, **kwargs):
		ctx = super(ProgramacionListView, self).get_context_data(**kwargs)
		ctx['inspectores'] = Usuario.objects.filter(inspector=True)

		inspector = self.request.GET.get('cmbInspectores', '')
		ctx['ejecutada']= self.request.GET.get('cmbEjecutada', '')
		if inspector and inspector !='0':
			ctx['inspectorSeleccionado'] = Usuario.objects.get(pk=inspector)
		else:
			ctx['inspectorSeleccionado'] = None

		ctx['query']= self.request.GET.get('q', '')		
		return ctx

class ProgramacionCreateView(CreateView):
	model = Programacion
	template_name='programacion/programacion-form.html'
	form_class = ProgramacionForm		
	
	def get_success_url(self):
		messages.success(self.request, 'La inspeccion ha sido programada exitosamente!')
		return reverse('agenda.agenda-list')

	def get_context_data(self,**kwargs):
		context = super(ProgramacionCreateView, self).get_context_data(**kwargs)
		context['titulo']='Agendar inspeccion'
		context['nombre_btn']='Guardar'
		return context

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('programacion.add_programacion'):
			return redirect(settings.LOGIN_URL)
		return super(ProgramacionCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(ProgramacionCreateView,self).form_valid(form)

	def get_form_kwargs(self, **kwargs):
		kwargs = super(ProgramacionCreateView, self).get_form_kwargs(**kwargs)
		kwargs['initial']['owner'] = self.request.user.id
		return kwargs
