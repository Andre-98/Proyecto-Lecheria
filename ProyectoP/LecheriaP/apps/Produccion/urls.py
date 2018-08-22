from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url, include

from apps.Produccion.views import index, Produccion_view, Produccion_list, Produccion_edit, Produccion_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', Produccion_view, name='Produccion_crear'),
    url(r'^listas$', Produccion_list, name='Produccion_listas'),
    url(r'^editar/(?P<id_Produccion>\d+)/$', Produccion_edit, name='Produccion_editar'),
    url(r'^eliminar/(?P<id_Produccion>\d+)/$', Produccion_delete, name='Produccion_eliminar'),
]