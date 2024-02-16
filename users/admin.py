from django.contrib import admin
from users.models import Usuario,Cuota


class CuotaInline(admin.TabularInline):
    model = Cuota
    fields = ('mes','fecha','metodo','al_dia')
    extra = 50
    can_delete = True

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_per_page = 50
    inlines = [CuotaInline]
