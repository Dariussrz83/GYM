from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from users.models import Usuario,Cuota



class CuotaInline(admin.TabularInline):
    model = Cuota
    fields = ('mes','fecha','metodo','al_dia')
    extra = 50
    can_delete = True



class Usuarioresource(resources.ModelResource):
    fields = (
        'nombre',
        'apellido',
        'celular',
    )
    class Meta:
        model = Usuario



@admin.register(Usuario)
class UsuarioAdmin(ImportExportModelAdmin):
    resource_class = Usuarioresource
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_per_page = 50
    inlines = [CuotaInline]