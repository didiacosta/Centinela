from django.conf.urls import patterns,url

from .views import InspeccionCreateView, InspeccionListView

urlpatterns = [

    url(r'^seguimiento/$', InspeccionListView.as_view(), name='inspeccion.inspeccion-list'),
    url(r'^registrarInspeccion/(?P<id>[0-9]+)/$', InspeccionCreateView.as_view(), name='inspeccion.registrarInspeccion'),
    # url(r'^editarDictamen/(?P<pk>[\w\-]+)/$', DictamenUpdateView.as_view(), name='dictamen.editarDictamen'),
    # url(r'^crearDictamen/$', DictamenCreateView.as_view(), name='dictamen.crearDictamen'),
    # url(r'^detalleDictamen/(?P<idDictamen>[\w\-]+)/$', DictamenDetailView.as_view(), name='Dictamen.Dictamen-detalle'),
    # url(r'^guardarEvaluacion/$', guardarEvaluacion, name='dictamen.guardarEvaluacion'),

]