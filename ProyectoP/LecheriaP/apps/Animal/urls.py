from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url, include

from apps.Animal.views import index, Animal_view, Animal_list, Animal_edit, Animal_delete

#app_name='Animal'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', Animal_view, name='Animal_crear'),
    url(r'^listas$', Animal_list, name='Animal_listas'),
    url(r'^editar/(?P<id_Animal>\d+)/$', Animal_edit, name='Animal_editar'),
    url(r'^eliminar/(?P<id_Animal>\d+)/$', Animal_delete, name='Animal_eliminar'),
]