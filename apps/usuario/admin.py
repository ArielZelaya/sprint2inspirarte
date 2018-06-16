# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Puesto)
admin.site.register(Contrato)