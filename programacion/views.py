from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Programacion
from usuario.models import Usuario

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings

from .forms import ProgramacionForm
# Create your views here.

class ProgramacionListView(ListView):
	model=Programacion
	template_name = 'programacion/programacion-list.html'
	paginate_by = 20


	def get_queryset(self):
		usuario= Usuario.objects.get(user=self.request.user)
		query = self.request.GET.get('q', '')
		if query:
			if usuario.coordinador:
				queryset = self.model.objects.filter(ordenServicio__icontains=query).order_by('-fecha')
			else:
				queryset= self.model.objects.filter(inspector=usuario,ordenServicio__icontains=query).order_by('-fecha')			
		else:
			if usuario.coordinador:
				queryset = self.model.objects.all().order_by('-fecha')
			else:
				queryset= self.model.objects.filter(inspector=usuario).order_by('-fecha')

		return queryset

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
