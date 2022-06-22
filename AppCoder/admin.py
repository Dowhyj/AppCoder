from django.contrib import admin

from .models import Familiar

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'fecha_nacimiento')

admin.site.register(Familiar, FamiliarAdmin)
