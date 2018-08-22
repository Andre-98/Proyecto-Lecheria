from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url, include

from apps.Inventario.views import index, Inventario_view, Inventario_list, Inventario_edit, Inventario_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', Inventario_view, name='Inventario_crear'),
    url(r'^listas$', Inventario_list, name='Inventario_listas'),
    url(r'^editar/(?P<id_Inventario>\d+)/$', Inventario_edit, name='Inventario_editar'),
    url(r'^eliminar/(?P<id_Inventario>\d+)/$', Inventario_delete, name='Inventario_eliminar'),
]