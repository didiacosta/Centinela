from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Inspeccion
from usuario.models import Usuario

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings

from .forms import InspeccionForm

from django.db.models import Q

class InspeccionCreateView(CreateView):
	model = Inspeccion
	template_name='inspeccion/inspeccion-form.html'
	form_class = InspeccionForm		
	
	def get_success_url(self):
		messages.success(self.request, 'La inspeccion ha sido registrada exitosamente!')
		return reverse('agenda.agenda-list')

	def get_context_data(self,**kwargs):
		context = super(InspeccionCreateView, self).get_context_data(**kwargs)
		context['titulo']='Reportar inspeccion'
		context['nombre_btn']='Reportar'
		context['programacion_id']=self.kwargs['id']
		return context

	def dispatch(self,request,*args, **kwargs):
		if not request.user.has_perms('inspeccion.add_inspeccion'):
			return redirect(settings.LOGIN_URL)
		return super(InspeccionCreateView, self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		form.instance.owner = self.request.user
		return super(InspeccionCreateView,self).form_valid(form)

	def get_form_kwargs(self, **kwargs):
		kwargs = super(InspeccionCreateView, self).get_form_kwargs(**kwargs)
		kwargs['initial']['owner'] = self.request.user.id
		return kwargs

	def get_form_kwargs(self):
		kwargs = super(InspeccionCreateView, self).get_form_kwargs()
		kwargs.update({'id': self.kwargs['id']})
		return kwargs

class InspeccionListView(ListView):
	model=Inspeccion
	template_name = 'inspeccion/inspeccion-list.html'
	#paginate_by = 20


	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		query = self.request.GET.get('q', '')
		inspector = self.request.GET.get('cmbInspectores', '')

		qset=(~Q(id=0))

		if query:
			qset=qset & (Q(programacion__ordenServicio__icontains=query) | Q(programacion__nombreProyecto__icontains=query))
		if usuario.coordinador==False:
			qset=qset & (Q(programacion__inspector=usuario))
		else:
			if inspector and inspector !='0':
				objInspector = Usuario.objects.get(pk=inspector)
				if objInspector:
					qset=qset & (Q(programacion__inspector=objInspector))

		queryset = self.model.objects.filter(qset)


		return queryset

	def get_context_data(self, **kwargs):
		ctx = super(InspeccionListView, self).get_context_data(**kwargs)
		ctx['inspectores'] = Usuario.objects.filter(inspector=True)

		inspector = self.request.GET.get('cmbInspectores', '')
		if inspector and inspector !='0':
			ctx['inspectorSeleccionado'] = Usuario.objects.get(pk=inspector)
		else:
			ctx['inspectorSeleccionado'] = None

		ctx['query']= self.request.GET.get('q', '')		
		return ctx

class InspeccionTabularListView(ListView):
	model=Inspeccion
	template_name = 'inspeccion/inspeccion-listTable.html'
	paginate_by = 10


	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		query = self.request.GET.get('q', '')
		inspector = self.request.GET.get('cmbInspectores', '')

		qset=(~Q(id=0))

		if query:
			qset=qset & (Q(programacion__ordenServicio__icontains=query) | Q(programacion__nombreProyecto__icontains=query))
		if usuario.coordinador==False:
			qset=qset & (Q(programacion__inspector=usuario))
		else:
			if inspector and inspector !='0':
				objInspector = Usuario.objects.get(pk=inspector)
				if objInspector:
					qset=qset & (Q(programacion__inspector=objInspector))

		queryset = self.model.objects.filter(qset)


		return queryset

	def get_context_data(self, **kwargs):
		ctx = super(InspeccionTabularListView, self).get_context_data(**kwargs)
		ctx['inspectores'] = Usuario.objects.filter(inspector=True)

		inspector = self.request.GET.get('cmbInspectores', '')
		if inspector and inspector !='0':
			ctx['inspectorSeleccionado'] = Usuario.objects.get(pk=inspector)
		else:
			ctx['inspectorSeleccionado'] = None

		ctx['query']= self.request.GET.get('q', '')		
		return ctx

