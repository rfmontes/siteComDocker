from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from cadastros.models import Motorista, Empresa, Caminhao, Material, Grupo


# def get_empresa(self, obj):
#     return ", ".join([str(p) for p in object.empresa.all()])


class MotoristaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'cpf', 'categoria_cnh', 'empresas', 'data_criacao', 'data_alteracao']
    search_fields = ['nome_completo', 'cpf']


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_empresa', 'cnpj', 'uf', 'telefone1', 'telefone2', 'data_criacao', 'data_alteracao']
    search_fields = ['nome_empresa', 'cnpj']


class CaminhaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'placa', 'marca', 'cor', 'empresas', 'data_criacao', 'data_alteracao']
    search_fields = ['placa']


class MaterialAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['nome_material', 'preco_material', 'nome_grupo', 'tipo', 'data_alteracao']
    search_fields = ['nome_material', 'nome_grupo']
    list_filter = ['nome_grupo', 'nome_material', 'data_criacao']


class GrupoAdmin(admin.ModelAdmin):
    list_display = ['nome_grupo', 'preco_grupo', 'data_criacao', 'data_alteracao']
    search_fields = ['nome_grupo']
    list_filter = ['nome_grupo', 'data_criacao']


admin.site.register(Motorista, MotoristaAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Caminhao, CaminhaoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Grupo, GrupoAdmin)

