from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Empresa(models.Model):
    CHOICE_UF = [
        ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'),
        ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'),
        ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'),
        ('SE', 'SE'), ('TO', 'TO'),
    ]
    nome_empresa = models.CharField(max_length=50, unique=True, verbose_name='Nome da Empresa')
    cnpj = models.CharField(max_length=20, unique=True, verbose_name='CNPJ')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    bairro = models.CharField(max_length=25, verbose_name='Bairro')
    cidade = models.CharField(max_length=20, verbose_name='Cidade')
    uf = models.CharField(max_length=3, choices=CHOICE_UF, verbose_name='UF')
    responsavel = models.CharField(max_length=50, null=True, blank=True, verbose_name='Responsável')
    telefone1 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone 1')
    telefone2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone 2')
    area_atuacao = models.CharField(max_length=50, null=True, blank=True, verbose_name='Área de Atuação')
    ativo = models.BooleanField(default=True)
    # data = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nome_empresa


class Motorista(models.Model):
    CATEGORIAS_CNH = [
        ('AB', 'AB'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'),
    ]
    cpf = models.CharField(max_length=15, unique=True, verbose_name='CPF')
    nome_completo = models.CharField(max_length=100, verbose_name='Nome Completo')
    cnh = models.CharField(max_length=15, unique=True, verbose_name='CNH')
    categoria_cnh = models.CharField(max_length=2, choices=CATEGORIAS_CNH, verbose_name='Categoria CNH')
    empresa = models.ManyToManyField(Empresa)
    ativo = models.BooleanField(default=True)
    # data = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def empresas(self):
        return ', '.join([empresa.nome_empresa for empresa in self.empresa.all()[:3]])

    def __str__(self):
        return self.cpf

    class Meta:
        ordering = ['nome_completo']


class Caminhao(models.Model):
    placa = models.CharField(max_length=9, unique=True, verbose_name='Placa')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20, verbose_name='Modelo')
    cor = models.CharField(max_length=20, verbose_name='Cor')
    empresa = models.ManyToManyField(Empresa)
    ativo = models.BooleanField(default=True)
    # data = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def empresas(self):
        return ', '.join([empresa.nome_empresa for empresa in self.empresa.all()[:3]])

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name = 'Caminhão'
        verbose_name_plural = 'Caminhões'
        ordering = ['marca']


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=50, unique=True, verbose_name='Grupo de Materiais')
    preco_grupo = models.DecimalField(max_digits=8, decimal_places=2, default=1, blank=True, null=True,
                                      verbose_name='Preço do Grupo de Materiais')
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nome_grupo

    class Meta:
        ordering = ['nome_grupo']


class Material(models.Model):
    CHOICE_TIPO = [('Entrega', 'Entrega'), ('Coleta', 'Coleta'), ]
    nome_material = models.CharField(max_length=50, unique=True, verbose_name='Material')
    preco_material = models.DecimalField(max_digits=8, decimal_places=2, default=1, blank=True, null=True,
                                         verbose_name='Preço do Material (por Tonelada)')
    nome_grupo = models.ForeignKey(Grupo, default=None, blank=True, null=True, on_delete=models.CASCADE,
                                   verbose_name='Grupo de Materiais')
    tipo = models.CharField(max_length=10, default=None, choices=CHOICE_TIPO, verbose_name='Evento')
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)
    minha_ordem = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return self.nome_material

    class Meta:
        verbose_name_plural = 'Materiais'
        ordering = ['minha_ordem']
