from django.contrib import admin


#imortamos las clases desde los modelos
from .models import Roles, DatosUser, HabiUser, DataRoles, Rates

# Register your models here.
admin.site.register(Roles)
admin.site.register(DatosUser)
admin.site.register(HabiUser)
admin.site.register(DataRoles)
admin.site.register(Rates)
