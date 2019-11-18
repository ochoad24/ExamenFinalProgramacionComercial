from django.contrib import admin
from sistema.models import Materia, GradoAdmin, Grado, MateriaAdmin

#Registramos nuestras clases principales.
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)