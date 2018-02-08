from django.conf.urls import patterns,url

from programacion.views import ProgramacionListView , ProgramacionCreateView#, DictamenUpdateView, DictamenDetailView

urlpatterns = [

    url(r'^agenda/$', ProgramacionListView.as_view(), name='agenda.agenda-list'),
    url(r'^agendarInspeccion/$', ProgramacionCreateView.as_view(), name='agenda.agendarInspeccion'),
    # url(r'^editarDictamen/(?P<pk>[\w\-]+)/$', DictamenUpdateView.as_view(), name='dictamen.editarDictamen'),
    # url(r'^crearDictamen/$', DictamenCreateView.as_view(), name='dictamen.crearDictamen'),
    # url(r'^detalleDictamen/(?P<idDictamen>[\w\-]+)/$', DictamenDetailView.as_view(), name='Dictamen.Dictamen-detalle'),
    # url(r'^guardarEvaluacion/$', guardarEvaluacion, name='dictamen.guardarEvaluacion'),

]