from django.contrib import admin
from eventos.models import Coleta, Entrega


class ColetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'empresa_nome', 'grupo', 'materiais', 'peso_carga', 'valor_carga_total',
                    'data_criacao', 'data_alteracao']
    search_fields = ['material', 'grupo', 'data_criacao']
    list_filter = ['data_criacao', 'material', 'grupo']


class EntregaAdmin(admin.ModelAdmin):
    list_display = ['id', 'empresa_nome', 'material', 'data_criacao', 'data_alteracao']
    search_fields = ['material', 'data_criacao']
    list_filter = ['data_criacao']


admin.site.register(Coleta, ColetaAdmin)
admin.site.register(Entrega, EntregaAdmin)