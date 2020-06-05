import csv
import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cadastros.forms import MotoristaForm, EmpresaForm, CaminhaoForm, MaterialForm, GrupoForm
from cadastros.models import Motorista, Caminhao, Empresa, Material, Grupo


@login_required(login_url='/login/')
def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits': num_visits, }
    return render(request, 'cadastros/index.html', context)


@permission_required('cadastros.add_motorista', login_url='/')
@login_required(login_url='/login/')
def cadastro_motorista(request):
    if request.method == 'GET':
        form = MotoristaForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastros/motorista.html', context)
    elif request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.usuario = request.user
            usuario.ativo = True
            usuario.save()
            form.save_m2m()
            messages.success(request, 'Motorista cadastrado com sucesso!')
            return render(request, 'cadastros/index.html')
        else:
            context = {
                'form': form,
            }
            return render(request, 'cadastros/motorista.html', context)


@permission_required('cadastros.view_motorista', login_url='/')
@login_required(login_url='/login/')
def lista_motorista(request):
    lista_total = Motorista.objects.filter(ativo=True).order_by('nome_completo')
    paginacao = Paginator(lista_total, 10)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'cadastros/motorista_lista.html', context)


@permission_required('cadastros.view_motorista', login_url='/')
@login_required(login_url='/login/')
def buscar_motorista(request):
    lista_total = Motorista.objects.filter(ativo=True).order_by('nome_completo')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_motorista:
            lista_nome = lista_total.filter(nome_completo__icontains=busca)
            lista_cpf = lista_total.filter(cpf__icontains=busca)
    lista_total = lista_cpf | lista_nome
    context = {'lista': lista_total}
    return render(request, 'cadastros/motorista_busca.html', context)


@permission_required('cadastros.view_motorista', login_url='/')
@login_required(login_url='/login/')
def detalhes_motorista(request, pk):
    motorista = Motorista.objects.get(pk=pk)
    context = {'motorista': motorista}
    return render(request, 'cadastros/motorista_detalhes.html', context)


@permission_required('cadastros.change_motorista', login_url='/')
@login_required(login_url='/login/')
def editar_motorista(request, pk):
    motorista = Motorista.objects.get(pk=pk)
    context = {'motorista': motorista}
    form = MotoristaForm(request.POST or None, instance=motorista)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.usuario = request.user
        usuario.ativo = True
        usuario.save()
        form.save_m2m()
        messages.success(request, 'Cadastro de motorista alterado com sucesso!')
        return render(request, 'cadastros/motorista_detalhes.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'cadastros/motorista.html', context)


@permission_required('cadastros.change_motorista', login_url='/')
@login_required(login_url='/login/')
def export_csv_motorista(request):
    motoristas = Motorista.objects.filter(ativo=True)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="motoristas.csv"'
    writer = csv.writer(response)
    writer.writerow(['CPF', 'Nome Completo', 'Numero CNH', 'Cat. CNH', 'Data cadastro', 'Usuario'])
    for motorista in motoristas:
        writer.writerow([motorista.cpf, motorista.nome_completo, motorista.cnh, motorista.categoria_cnh,
                         motorista.data_criacao, motorista.usuario])
    return response


@permission_required('cadastros.change_motorista', login_url='/')
@login_required(login_url='/login/')
def export_xlsx_motorista(request):
    pass


@permission_required('cadastros.add_caminhao', login_url='/')
@login_required(login_url='/login/')
def cadastro_caminhao(request):
    if request.method == 'GET':
        form = CaminhaoForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastros/caminhao.html', context)
    elif request.method == 'POST':
        form = CaminhaoForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.usuario = request.user
            usuario.ativo = True
            usuario.save()
            form.save_m2m()
            messages.success(request, 'Caminhão cadastrado com sucesso!')
            return render(request, 'cadastros/index.html')
        else:
            context = {
                'form': form,
            }
            return render(request, 'cadastros/caminhao.html', context)


@permission_required('cadastros.view_caminhao', login_url='/')
@login_required(login_url='/login/')
def lista_caminhao(request):
    lista_total = Caminhao.objects.filter(ativo=True).order_by('placa')
    paginacao = Paginator(lista_total, 10)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'cadastros/caminhao_lista.html', context)


@permission_required('cadastros.view_caminhao', login_url='/')
@login_required(login_url='/login/')
def buscar_caminhao(request):
    lista_total = Caminhao.objects.filter(ativo=True).order_by('placa')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_caminhao:
            lista_placa = lista_total.filter(placa__icontains=busca)
            lista_marca = lista_total.filter(marca__icontains=busca)
    lista_total = lista_marca | lista_placa
    context = {'lista': lista_total}
    return render(request, 'cadastros/caminhao_busca.html', context)


@permission_required('cadastros.view_caminhao', login_url='/')
@login_required(login_url='/login/')
def detalhes_caminhao(request, pk):
    caminhao = Caminhao.objects.get(pk=pk)
    context = {'caminhao': caminhao}
    return render(request, 'cadastros/caminhao_detalhes.html', context)


@permission_required('cadastros.change_caminhao', login_url='/')
@login_required(login_url='/login/')
def editar_caminhao(request, pk):
    caminhao = Caminhao.objects.get(pk=pk)
    context = {'caminhao': caminhao}
    form = CaminhaoForm(request.POST or None, instance=caminhao)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.usuario = request.user
        usuario.ativo = True
        usuario.save()
        form.save_m2m()
        messages.success(request, 'Cadastro de caminhão alterado com sucesso!')
        return render(request, 'cadastros/caminhao_detalhes.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'cadastros/caminhao.html', context)


@permission_required('cadastros.change_caminhao', login_url='/')
@login_required(login_url='/login/')
def export_csv_caminhao(request):
    caminhoes = Caminhao.objects.filter(ativo=True)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="caminhoes.csv"'
    writer = csv.writer(response)
    writer.writerow(['Placa', 'Marca', 'Modelo', 'Cor', 'Data cadastro', 'Usuario'])
    for caminhao in caminhoes:
        writer.writerow([caminhao.placa, caminhao.marca, caminhao.modelo, caminhao.cor, caminhao.data_criacao,
                         caminhao.usuario])
    return response


@permission_required('cadastros.change_caminhao', login_url='/')
@login_required(login_url='/login/')
def export_xlsx_caminhao(request):
    pass


@permission_required('cadastros.add_empresa', login_url='/')
@login_required(login_url='/login/')
def cadastro_empresa(request):
    if request.method == 'GET':
        form = EmpresaForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastros/empresa.html', context)
    elif request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.ativo = True
            form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return render(request, 'cadastros/index.html')
        else:
            context = {
                'form': form,
            }
            return render(request, 'cadastros/empresa.html', context)


@permission_required('cadastros.view_empresa', login_url='/')
@login_required(login_url='/login/')
def lista_empresa(request):
    lista_total = Empresa.objects.filter(ativo=True).order_by('nome_empresa')
    paginacao = Paginator(lista_total, 10)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'cadastros/empresa_lista.html', context)


@permission_required('cadastros.view_empresa', login_url='/')
@login_required(login_url='/login/')
def buscar_empresa(request):
    lista_total = Empresa.objects.filter(ativo=True).order_by('nome_empresa')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_empresa:
            lista_nome = lista_total.filter(nome_empresa__icontains=busca)
            lista_cnpj = lista_total.filter(cnpj__icontains=busca)
    lista_total = lista_nome | lista_cnpj
    context = {'lista': lista_total}
    return render(request, 'cadastros/empresa_busca.html', context)


@permission_required('cadastros.view_empresa', login_url='/')
@login_required(login_url='/login/')
def detalhes_empresa(request, pk):
    empresa = Empresa.objects.get(pk=pk)
    context = {'empresa': empresa}
    return render(request, 'cadastros/empresa_detalhes.html', context)


@permission_required('cadastros.change_empresa', login_url='/')
@login_required(login_url='/login/')
def editar_empresa(request, pk):
    empresa = Empresa.objects.get(pk=pk)
    context = {'empresa': empresa}
    form = EmpresaForm(request.POST or None, instance=empresa)
    if form.is_valid():
        form = form.save(commit=False)
        form.usuario = request.user
        form.ativo = True
        form.save()
        messages.success(request, 'Cadastro da empresa alterado com sucesso!')
        return render(request, 'cadastros/empresa_detalhes.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'cadastros/empresa.html', context)


@permission_required('cadastros.change_empresa', login_url='/')
@login_required(login_url='/login/')
def export_csv_empresa(request):
    empresas = Empresa.objects.filter(ativo=True)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="empresas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nome', 'CNPJ', 'CEP', 'Endereço', 'Bairro', 'Cidade', 'UF', 'Responsavel', 'Telefone1',
                     'Telefone2', 'Area de Atuação', 'Data cadastro', 'Usuario'])
    for empresa in empresas:
        writer.writerow([empresa.nome_empresa, empresa.cnpj, empresa.cep, empresa.endereco, empresa.bairro,
                         empresa.cidade, empresa.uf, empresa.responsavel, empresa.telefone1, empresa.telefone2,
                         empresa.area_atuacao, empresa.data_criacao, empresa.usuario])
    return response


@permission_required('cadastros.change_empresa', login_url='/')
@login_required(login_url='/login/')
def export_xlsx_empresa(request):
    pass


@permission_required('cadastros.add_material', login_url='/')
@login_required(login_url='/login/')
def cadastro_material(request):
    if request.method == 'GET':
        form = MaterialForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastros/material.html', context)
    elif request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.ativo = True
            n = 1000
            form.minha_ordem = random.randint(1, 10000) + n
            form.save()
            messages.success(request, 'Material cadastrado com sucesso!')
            return render(request, 'cadastros/index.html')
        else:
            context = {
                'form': form,
            }
            return render(request, 'cadastros/material.html', context)


@permission_required('cadastros.view_material', login_url='/')
@login_required(login_url='/login/')
def lista_material(request):
    lista_total = Material.objects.filter(ativo=True).order_by('minha_ordem')
    paginacao = Paginator(lista_total, 25)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'cadastros/material_lista.html', context)


@permission_required('cadastros.view_material', login_url='/')
@login_required(login_url='/login/')
def buscar_material(request):
    lista_total = Material.objects.filter(ativo=True).order_by('nome_material')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_material:
            lista_material = lista_total.filter(nome_material__icontains=busca)
            # lista_grupo = lista_total.filter(nome_grupo__icontains=busca)
    lista_total = lista_material
    context = {'lista': lista_total}
    return render(request, 'cadastros/material_busca.html', context)


@permission_required('cadastros.view_material', login_url='/')
@login_required(login_url='/login/')
def detalhes_material(request, pk):
    material = Material.objects.get(pk=pk)
    context = {'material': material}
    return render(request, 'cadastros/material_detalhes.html', context)


@permission_required('cadastros.change_material', login_url='/')
@login_required(login_url='/login/')
def editar_material(request, pk):
    material = Material.objects.get(pk=pk)
    context = {'material': material}
    form = MaterialForm(request.POST or None, instance=material)
    if form.is_valid():
        form = form.save(commit=False)
        form.usuario = request.user
        form.ativo = True
        form.save()
        messages.success(request, 'Cadastro do material alterado com sucesso!')
        return render(request, 'cadastros/material_detalhes.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'cadastros/material.html', context)


@permission_required('cadastros.change_material', login_url='/')
@login_required(login_url='/login/')
def export_csv_material(request):
    materiais = Material.objects.filter(ativo=True)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="materiais.csv"'
    writer = csv.writer(response)
    writer.writerow(['Material', 'Preço', 'Grupo', 'Data cadastro', 'Usuario'])
    for material in materiais:
        writer.writerow([material.nome_material, material.preco_material, material.nome_grupo, material.data_criacao,
                         material.usuario])
    return response


@permission_required('cadastros.change_material', login_url='/')
@login_required(login_url='/login/')
def export_xlsx_material(request):
    pass
    # response = HttpResponse(content_type='application/ms-excel')
    # response['Content-Disposition'] = 'attachment; filename="materiais.xls"'
    #
    # wb = xlwt.Workbook(encoding='utf-8')
    # ws = wb.add_sheet('Material')
    #
    # row_num = 0
    #
    # font_style = xlwt.XFStyle()
    # font_style.font.bold = True
    #
    # colunas = ('Material', 'Preço', 'Grupo', 'Usuario')
    #
    # for col_num in range(len(colunas)):
    #     ws.write(row_num, col_num, colunas[col_num], font_style)
    #
    # default_style = xlwt.XFStyle()
    #
    # rows = Material.objects.all().values_list('nome_material', 'preco_material', 'nome_grupo', 'usuario')
    # for row in rows:
    #     row_num += 1
    #     for col_num in range(len(row)):
    #         ws.write(row_num, col_num, row[col_num], default_style)
    #
    # wb.save(response)
    # return response


@permission_required('cadastros.add_grupo', login_url='/')
@login_required(login_url='/login/')
def cadastro_grupo(request):
    if request.method == 'GET':
        form = GrupoForm()
        context = {
            'form': form,
        }
        return render(request, 'cadastros/grupo.html', context)
    elif request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.ativo = True
            form.save()
            messages.success(request, 'Grupo cadastrado com sucesso!')
            return redirect(cadastro_material)
        else:
            context = {
                'form': form,
            }
            return render(request, 'cadastros/grupo.html', context)


@permission_required('cadastros.view_grupo', login_url='/')
@login_required(login_url='/login/')
def lista_grupo(request):
    lista_total = Grupo.objects.filter(ativo=True).order_by('nome_grupo')
    paginacao = Paginator(lista_total, 10)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'cadastros/grupo_lista.html', context)


@permission_required('cadastros.view_grupo', login_url='/')
@login_required(login_url='/login/')
def buscar_grupo(request):
    lista_total = Grupo.objects.filter(ativo=True).order_by('nome_grupo')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_grupo:
            lista_grupo = lista_total.filter(nome_grupo__icontains=busca)
    lista_total = lista_grupo
    context = {'lista': lista_total}
    return render(request, 'cadastros/grupo_busca.html', context)


@permission_required('cadastros.view_grupo', login_url='/')
@login_required(login_url='/login/')
def detalhes_grupo(request, pk):
    grupo = Grupo.objects.get(pk=pk)
    context = {'grupo': grupo}
    return render(request, 'cadastros/grupo_detalhes.html', context)


@permission_required('cadastros.change_grupo', login_url='/')
@login_required(login_url='/login/')
def editar_grupo(request, pk):
    grupo = Grupo.objects.get(pk=pk)
    context = {'grupo': grupo}
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form = form.save(commit=False)
        form.usuario = request.user
        form.ativo = True
        form.save()
        messages.success(request, 'Cadastro do grupo alterado com sucesso!')
        return render(request, 'cadastros/grupo_detalhes.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'cadastros/grupo.html', context)