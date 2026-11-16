from django.contrib import admin
from .models import Tarea, Programador, Sprint, Etiqueta, Proyecto

# Register your models here.

admin.site.register(Tarea)
admin.site.register(Programador)
admin.site.register(Sprint)
admin.site.register(Etiqueta)
admin.site.register(Proyecto)
