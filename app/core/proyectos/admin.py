from django.contrib import admin

#imortamos las clases desde los modelos
from .models import TipoDocu, CateProyecto, Proyecto, Documento

admin.site.register(TipoDocu)
admin.site.register(CateProyecto)
admin.site.register(Proyecto)
admin.site.register(Documento)