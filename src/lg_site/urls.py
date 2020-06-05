"""lg_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from cadastros.views import *

from eventos.views import *

from contas.views import criar_usuario, login_submit, login_usuario, logout_usuario, painel_controle, editar, \
    editar_senha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='url_index'),

    # URL para usar funcionalidades de recuperação de senha do Django
    path('accounts/', include('django.contrib.auth.urls')),

    path('login/', login_usuario, name='url_login'),
    path('login/submit', login_submit),
    path('logout/', logout_usuario, name='url_logout'),
    path('registro/', criar_usuario, name='url_cria_usuario'),
    path('painel/', painel_controle, name='url_painel_controle'),
    path('editar/', editar, name='url_editar'),
    path('editar/senha/', editar_senha, name='url_editar_senha'),

    path('motorista/', cadastro_motorista, name='url_cad_motorista'),
    path('motorista/listagem', lista_motorista, name='url_lista_motorista'),
    path('motorista/listagem/editar/<int:pk>', editar_motorista, name='url_editar_motorista'),
    path('motorista/listagem/detalhes/<int:pk>', detalhes_motorista, name='url_detalhes_motorista'),
    path('motorista/listagem/busca/', buscar_motorista, name='url_busca_motorista'),
    path('motorista/listagem/exportar/csv', export_csv_motorista, name='url_exportar_csv_motorista'),

    path('caminhao/', cadastro_caminhao, name='url_cad_caminhao'),
    path('caminhao/listagem', lista_caminhao, name='url_lista_caminhao'),
    path('caminhao/listagem/detalhes/<int:pk>', detalhes_caminhao, name='url_detalhes_caminhao'),
    path('caminhao/listagem/editar/<int:pk>', editar_caminhao, name='url_editar_caminhao'),
    path('caminhao/listagem/busca/', buscar_caminhao, name='url_busca_caminhao'),
    path('caminhao/listagem/exportar/csv', export_csv_caminhao, name='url_exportar_csv_caminhao'),

    path('empresa/', cadastro_empresa, name='url_cad_empresa'),
    path('empresa/listagem', lista_empresa, name='url_lista_empresa'),
    path('empresa/listagem/detalhes/<int:pk>', detalhes_empresa, name='url_detalhes_empresa'),
    path('empresa/listagem/editar/<int:pk>', editar_empresa, name='url_editar_empresa'),
    path('empresa/listagem/busca/', buscar_empresa, name='url_busca_empresa'),
    path('empresa/listagem/exportar/csv', export_csv_empresa, name='url_exportar_csv_empresa'),

    path('material/', cadastro_material, name='url_cad_material'),
    path('material/listagem', lista_material, name='url_lista_material'),
    path('material/listagem/detalhes/<int:pk>', detalhes_material, name='url_detalhes_material'),
    path('material/listagem/editar/<int:pk>', editar_material, name='url_editar_material'),
    path('material/listagem/busca/', buscar_material, name='url_busca_material'),
    path('material/listagem/exportar/csv', export_csv_material, name='url_exportar_csv_material'),

    path('material/grupo/', cadastro_grupo, name='url_cad_grupo'),
    path('grupo/listagem', lista_grupo, name='url_lista_grupo'),
    path('grupo/listagem/detalhes/<int:pk>', detalhes_grupo, name='url_detalhes_grupo'),
    path('grupo/listagem/editar/<int:pk>', editar_grupo, name='url_editar_grupo'),
    path('grupo/listagem/busca/', buscar_grupo, name='url_busca_grupo'),

    path('coleta/', cadastro_coleta, name='url_cad_coleta'),
    path('coleta/listagem', lista_coleta, name='url_lista_coleta'),
    path('coleta/listagem/detalhes/<int:pk>', detalhes_coleta, name='url_detalhes_coleta'),
    path('coleta/listagem/editar/<int:pk>', editar_coleta, name='url_editar_coleta'),
    path('coleta/listagem/busca/', buscar_coleta, name='url_busca_coleta'),
    path('coleta/listagem/exportar/csv', export_csv_coleta, name='url_exportar_csv_coleta'),

    path('entrega/', cadastro_entrega, name='url_cad_entrega'),
    path('entrega/listagem', lista_entrega, name='url_lista_entrega'),
    path('entrega/listagem/detalhes/<int:pk>', detalhes_entrega, name='url_detalhes_entrega'),
    path('entrega/listagem/editar/<int:pk>', editar_entrega, name='url_editar_entrega'),
    path('entrega/listagem/busca/', buscar_entrega, name='url_busca_entrega'),
    path('entrega/listagem/exportar/csv', export_csv_entrega, name='url_exportar_csv_entrega'),

    path('coleta/listagem/exportar/xlsx', export_xlsx_coleta, name='url_exportar_xlsx_coleta'),
    path('entrega/listagem/exportar/xlsx', export_xlsx_entrega, name='url_exportar_xlsx_entrega'),
    path('motorista/listagem/exportar/xlsx', export_xlsx_motorista, name='url_exportar_xlsx_motorista'),
    path('caminhao/listagem/exportar/xlsx', export_xlsx_caminhao, name='url_exportar_xlsxv_caminhao'),
    path('empresa/listagem/exportar/xlsx', export_xlsx_empresa, name='url_exportar_xlsx_empresa'),
    path('material/listagem/exportar/xlsx', export_xlsx_material, name='url_exportar_xlsx_material'),

    path('motorista/choices/ajax/', motorista_choices_ajax, name='url_motorista_choices_ajax'),
    path('caminhao/choices/ajax/', caminhao_choices_ajax, name='url_caminhao_choices_ajax'),
]
