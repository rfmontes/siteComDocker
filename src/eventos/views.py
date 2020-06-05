import csv

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from cadastros.models import Motorista, Caminhao
from eventos.forms import ColetaForm, EntregaForm
from eventos.models import Coleta, Entrega
from eventos.valor import valorAluminio, valorCobre, valorChumbo, valorNiquel, valorEstanho, valorZinco, \
    valorVergalhoesAco, valorSucataAco


@permission_required('eventos.add_coleta', login_url='/')
@login_required(login_url='/login/')
def cadastro_coleta(request):
    if request.method == 'GET':
        form = ColetaForm()
        context = {
            'form': form,
        }
        return render(request, 'eventos/coleta.html', context)
    elif request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            coleta = form.save(commit=False)
            coleta.usuario = request.user
            coleta.peso_carga = coleta.peso_carregado - coleta.peso_vazio

            # if coleta.grupo is not None:
            #     print(coleta.grupo)
            #     coleta.valor_carga_total = (coleta.grupo.preco_grupo * (coleta.peso_carregado - coleta.peso_vazio)) / 1000
            # else:
            #     print('Grupo é None')
            #
            # if coleta.material is not None:
            #     print(coleta.material)
            #     # if form.material.nome_material == 'Alumínio' or form.material.nome_material == 'Aluminio':
            #     #     form.material.preco_material = valorAluminio()
            #     # elif form.material.nome_material == 'Cobre':
            #     #     form.material.preco_material = valorCobre()
            #     # elif form.material.nome_material == 'Chumbo':
            #     #     form.material.preco_material = valorChumbo()
            #     # elif form.material.nome_material == 'Níquel' or form.material.nome_material == 'Niquel':
            #     #     form.material.preco_material = valorNiquel()
            #     # elif form.material.nome_material == 'Estanho':
            #     #     form.material.preco_material = valorEstanho()
            #     # elif form.material.nome_material == 'Zinco':
            #     #     form.material.preco_material = valorZinco()
            #     # elif form.material.nome_material == 'Vergalhões de aço':
            #     #     form.material.preco_material = valorVergalhoesAco()
            #     # elif form.material.nome_material == 'Sucata de aço':
            #     #     form.material.preco_material = valorSucataAco()
            #     # form.valor_carga_total = (form.material.preco_material * (form.peso_carregado - form.peso_vazio)) / 1000
            #     coleta.valor_carga_total = 0
            # else:
            #     print('Material é None')

            coleta.save()
            form.save_m2m()
            messages.success(request, 'Coleta cadastrada com sucesso!')
            return render(request, 'cadastros/index.html')
        else:
            context = {
                'form': form,
            }
            return render(request, 'eventos/coleta.html', context)


@permission_required('eventos.add_coleta', login_url='/')
@login_required(login_url='/login/')
def motorista_choices_ajax(request):
    empresa = request.GET.get('empresa')
    motoristas = Motorista.objects.filter(empresa=empresa)
    context = {'motoristas': motoristas}
    return render(request, 'eventos/_motoristas_choices.html', context)


@permission_required('eventos.add_coleta', login_url='/')
@login_required(login_url='/login/')
def caminhao_choices_ajax(request):
    empresa = request.GET.get('empresa')
    caminhoes = Caminhao.objects.filter(empresa=empresa)
    context = {'caminhoes': caminhoes}
    return render(request, 'eventos/_caminhoes_choices.html', context)


@permission_required('eventos.view_coleta', login_url='/')
@login_required(login_url='/login/')
def lista_coleta(request):
    lista_total = Coleta.objects.all().order_by('-data_criacao')
    paginacao = Paginator(lista_total, 10)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'eventos/coleta_lista.html', context)


@permission_required('eventos.view_coleta', login_url='/')
@login_required(login_url='/login/')
def buscar_coleta(request):
    lista_total = Coleta.objects.all().order_by('-data_criacao')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_coleta:
            lista_data = lista_total.filter(data_criacao__icontains=busca)
    lista_total = lista_data
    context = {'lista': lista_total}
    return render(request, 'eventos/coleta_busca.html', context)


@permission_required('eventos.view_coleta', login_url='/')
@login_required(login_url='/login/')
def detalhes_coleta(request, pk):
    coleta = Coleta.objects.get(pk=pk)
    context = {'coleta': coleta}
    return render(request, 'eventos/coleta_detalhes.html', context)


@permission_required('eventos.change_coleta', login_url='/')
@login_required(login_url='/login/')
def editar_coleta(request, pk):
    coleta = Coleta.objects.get(pk=pk)
    context = {'coleta': coleta}
    form = ColetaForm(request.POST or None, instance=coleta)
    if form.is_valid():
        coleta = form.save(commit=False)
        coleta.usuario = request.user
        coleta.peso_carga = coleta.peso_carregado - coleta.peso_vazio

        # if coleta.grupo is not None:
        #     print(coleta.grupo)
        #     coleta.valor_carga_total = (coleta.grupo.preco_grupo * (coleta.peso_carregado - coleta.peso_vazio)) / 1000
        # else:
        #     print(coleta.grupo)
        #     print('Grupo é None')
        #
        # if coleta.material is not None:
        #     print(coleta.material)
        #     # if form.material.nome_material == 'Alumínio' or form.material.nome_material == 'Aluminio':
        #     #     form.material.preco_material = valorAluminio()
        #     # elif form.material.nome_material == 'Cobre':
        #     #     form.material.preco_material = valorCobre()
        #     # elif form.material.nome_material == 'Chumbo':
        #     #     form.material.preco_material = valorChumbo()
        #     # elif form.material.nome_material == 'Níquel' or form.material.nome_material == 'Niquel':
        #     #     form.material.preco_material = valorNiquel()
        #     # elif form.material.nome_material == 'Estanho':
        #     #     form.material.preco_material = valorEstanho()
        #     # elif form.material.nome_material == 'Zinco':
        #     #     form.material.preco_material = valorZinco()
        #     # elif form.material.nome_material == 'Vergalhões de aço':
        #     #     form.material.preco_material = valorVergalhoesAco()
        #     # elif form.material.nome_material == 'Sucata de aço':
        #     #     form.material.preco_material = valorSucataAco()
        #     # form.valor_carga_total = (form.material.preco_material * (form.peso_carregado - form.peso_vazio)) / 1000
        #     coleta.valor_carga_total = 0
        # else:
        #     print('Material é None')

        coleta.save()
        form.save_m2m()
        messages.success(request, 'Cadastro da coleta alterado com sucesso!')
        return render(request, 'eventos/coleta_detalhes.html', context)
    else:
        context = {
            'form': form,
        }
        return render(request, 'eventos/coleta.html', context)


@permission_required('eventos.change_coleta', login_url='/')
@login_required(login_url='/login/')
def export_csv_coleta(request):
    coletas = Coleta.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="coletas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Quant. Retiradas', 'Tag RFID', 'Grupo', 'Material', 'CPF', 'Empresa', 'Caminhão',
                     'Peso do caminhão vazio', 'Peso do caminhão carregado', 'Peso da carga',
                     'Valor da carga', 'Data e Hora', 'Usuario'])
    for coleta in coletas:
        writer.writerow([coleta.quant_retiradas, coleta.cartao_numero, coleta.grupo, coleta.material,
                         coleta.motorista_cpf, coleta.empresa_nome, coleta.caminhao_placa, coleta.peso_vazio,
                         coleta.peso_carregado, coleta.peso_carga, coleta.valor_carga_total, coleta.data_criacao,
                         coleta.usuario])
    return response


@permission_required('eventos.change_coleta', login_url='/')
@login_required(login_url='/login/')
def export_xlsx_coleta(request):
    pass


@permission_required('eventos.add_entrega', login_url='/')
@login_required(login_url='/login/')
def cadastro_entrega(request):
    if request.method == 'GET':
        form = EntregaForm()
        context = {
            'form': form,
        }
        return render(request, 'eventos/entrega.html', context)
    elif request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.peso_carga = form.peso_vazio - form.peso_carregado
            form.valor_carga_total = (form.material.preco_material * (form.peso_vazio - form.peso_carregado)) / 1000
            form.save()
            messages.success(request, 'Entrega cadastrada com sucesso!')
            return render(request, 'cadastros/index.html')

        else:
            context = {
                'form': form,
            }
            return render(request, 'eventos/entrega.html', context)


@permission_required('eventos.view_entrega', login_url='/')
@login_required(login_url='/login/')
def lista_entrega(request):
    lista_total = Entrega.objects.all().order_by('-data_criacao')
    paginacao = Paginator(lista_total, 10)
    page = request.GET.get('page')
    lista = paginacao.get_page(page)
    context = {'lista': lista}
    return render(request, 'eventos/entrega_lista.html', context)


@permission_required('eventos.view_entrega', login_url='/')
@login_required(login_url='/login/')
def buscar_entrega(request):
    lista_total = Entrega.objects.all().order_by('-data_criacao')
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if buscar_entrega:
            lista_data = lista_total.filter(data_criacao__icontains=busca)
    lista_total = lista_data
    context = {'lista': lista_total}
    return render(request, 'eventos/entrega_busca.html', context)


@permission_required('eventos.view_entrega', login_url='/')
@login_required(login_url='/login/')
def detalhes_entrega(request, pk):
    entrega = Entrega.objects.get(pk=pk)
    context = {'entrega': entrega}
    return render(request, 'eventos/entrega_detalhes.html', context)


@permission_required('eventos.change_entrega', login_url='/')
@login_required(login_url='/login/')
def editar_entrega(request, pk):
    entrega = Entrega.objects.get(pk=pk)
    context = {'entrega': entrega}
    form = EntregaForm(request.POST or None, instance=entrega)
    if form.is_valid():
        form = form.save(commit=False)
        form.usuario = request.user
        form.peso_carga = form.peso_vazio - form.peso_carregado
        form.valor_carga_total = (form.material.preco_material * (form.peso_vazio - form.peso_carregado)) / 1000
        form.save()
        messages.success(request, 'Cadastro da entrega alterado com sucesso!')
        return render(request, 'eventos/entrega_detalhes.html', context)

    else:
        context = {
            'form': form,
        }
        return render(request, 'eventos/entrega.html', context)


@permission_required('eventos.change_entrega', login_url='/')
@login_required(login_url='/login/')
def export_csv_entrega(request):
    entregas = Entrega.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entregas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Tag RFID', 'Material', 'CPF', 'Empresa', 'Caminhão',
                     'Peso do caminhão carregado', 'Peso do caminhão vazio', 'Peso da carga', 'Data e Hora', 'Usuario'
                     ])
    for entrega in entregas:
        writer.writerow([entrega.cartao_numero, entrega.material_entrega, entrega.motorista_cpf, entrega.empresa_nome,
                         entrega.caminhao_placa, entrega.peso_carregado, entrega.peso_vazio, entrega.peso_carga,
                         entrega.data_criacao, entrega.usuario])
    return response


@permission_required('eventos.change_entrega', login_url='/')
@login_required(login_url='/login/')
def export_xlsx_entrega(request):
    pass


# @login_required(login_url='/login/')
# def export_csv(request):
#     header = ('quant_retiradas', 'cartao_numero', 'grupo', 'material', 'motorista_cpf', 'empresa_nome',
#               'caminhao_placa', 'peso_vazio', 'peso_carga1', 'valor_carga_total', 'data_criacao', 'usuario',
#               )
#     coletas = Coleta.objects.all().values_list(*header)
#     with open('teste_exportar/coletas_exportadas.csv', 'w') as csvfile:
#         coleta_writer = csv.writer(csvfile)
#         coleta_writer.writerow(header)
#         for coleta in coletas:
#             coleta_writer.writerow(coleta)
#     messages.success(request, 'Coletas exportadas com sucesso.')
#     return redirect(lista_coleta)
