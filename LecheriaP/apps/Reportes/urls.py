from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required

from apps.Reportes.views import index, Reportes_view, Reportes_list, Reportes_edit, Reportes_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(Reportes_view), name='Reportes_crear'),
    url(r'^listas$', login_required(Reportes_list), name='Reportes_listas'),
    url(r'^editar/(?P<id_Reportes>\d+)/$', login_required(Reportes_edit), name='Reportes_editar'),
    url(r'^eliminar/(?P<id_Reportes>\d+)/$', login_required(Reportes_delete), name='Reportes_eliminar'),
]