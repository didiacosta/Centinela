from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Inspeccion
from usuario.models import Usuario

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings

from .forms import InspeccionForm

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
		if query:
			if usuario.coordinador:
				queryset = self.model.objects.filter(programacion__ordenServicio__icontains=query)
			else:
				queryset= self.model.objects.filter(programacion__inspector=usuario,
					programacion__ordenServicio__icontains=query)
		else:
			if usuario.coordinador:
				queryset = self.model.objects.all()
			else:
				queryset= self.model.objects.filter(programacion__inspector=usuario)

		return queryset

