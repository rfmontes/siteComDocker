from django.contrib.auth import get_user_model
from django.db import models

from cadastros.models import Motorista, Empresa, Caminhao, Material, Grupo


class Coleta(models.Model):
    quant_retiradas = models.PositiveIntegerField(default=1, verbose_name='Retiradas')
    cartao_numero = models.CharField(max_length=50, verbose_name='Tag RFID')
    grupo = models.ForeignKey(Grupo, default=None, blank=True, null=True, on_delete=models.CASCADE,
                              verbose_name='Grupo de Materiais')
    material = models.ManyToManyField(Material, blank=True, verbose_name='Material')
    empresa_nome = models.ForeignKey(Empresa, default=None, on_delete=models.CASCADE, verbose_name='Nome da Empresa')
    motorista_cpf = models.ForeignKey(Motorista, default=None, on_delete=models.CASCADE,
                                      verbose_name='CPF do Motorista')
    caminhao_placa = models.ForeignKey(Caminhao, default=None, on_delete=models.CASCADE,
                                       verbose_name='Placa do Caminhão')
    peso_vazio = models.PositiveIntegerField(default=None, blank=True, verbose_name='Caminhão vazio (em Kg)')
    peso_carregado = models.PositiveIntegerField(default=None, verbose_name='Caminhão carregado (em Kg)')
    peso_carga = models.PositiveIntegerField(default=None, blank=True, null=True, verbose_name='Peso da carga (em Kg)')
    valor_carga_total = models.DecimalField(max_digits=15, decimal_places=2, default=None, blank=True, null=True,
                                            verbose_name='Valor da carga')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def materiais(self):
        return ', '.join([material.nome_material for material in self.material.all()[:3]])

    def __str__(self):
        return self.cartao_numero

    class Meta:
        ordering = ['-id']


class Entrega(models.Model):
    cartao_numero = models.CharField(max_length=50, verbose_name='Número do Cartão')
    material = models.ForeignKey(Material, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Material')
    motorista_cpf = models.ForeignKey(Motorista, default=None, on_delete=models.CASCADE, verbose_name='CPF do '
                                                                                                      'Motorista')
    empresa_nome = models.ForeignKey(Empresa, default=None, on_delete=models.CASCADE, verbose_name='Nome da Empresa')
    caminhao_placa = models.ForeignKey(Caminhao, default=None, on_delete=models.CASCADE, verbose_name='Placa do '
                                                                                                      'Caminhão')
    peso_carregado = models.PositiveIntegerField(default=None, verbose_name='Caminhão Carregado (em Kg)')
    peso_vazio = models.PositiveIntegerField(default=None, verbose_name='Caminhão vazio (em Kg)')
    peso_carga = models.PositiveIntegerField(default=None, blank=True, null=True, verbose_name='Peso da carga (em Kg)')
    valor_carga_total = models.DecimalField(max_digits=15, decimal_places=2, default=None, blank=True, null=True,
                                            verbose_name='Valor da carga')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_alteracao = models.DateTimeField(auto_now=True, verbose_name='Ultima Alteração')
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.cartao_numero

    class Meta:
        ordering = ['-id']
