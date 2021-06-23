from django.contrib import admin
from .models import baterias, filtros, aceites , Comment

model = baterias, filtros, aceites , Comment

admin.site.register(model)
