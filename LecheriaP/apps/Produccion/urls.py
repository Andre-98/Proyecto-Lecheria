from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required

from apps.Produccion.views import index, Produccion_view, Produccion_list, Produccion_edit, Produccion_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(Produccion_view), name='Produccion_crear'),
    url(r'^listas$', login_required(Produccion_list), name='Produccion_listas'),
    url(r'^editar/(?P<id_Produccion>\d+)/$', login_required(Produccion_edit), name='Produccion_editar'),
    url(r'^eliminar/(?P<id_Produccion>\d+)/$', login_required(Produccion_delete), name='Produccion_eliminar'),
]