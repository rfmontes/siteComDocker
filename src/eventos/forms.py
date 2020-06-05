from django import forms

from cadastros.models import Motorista, Caminhao, Material
from eventos.models import Coleta, Entrega


class ColetaForm(forms.ModelForm):
    class Meta:
        model = Coleta
        fields = '__all__'
        exclude = ['usuario', 'peso_carga', 'valor_carga_total', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grupo'].widget.attrs.update({'class': 'select form-control'})
        self.fields['material'].widget.attrs.update({'class': 'select form-control'})
        self.fields['motorista_cpf'].widget.attrs.update({'class': 'select form-control'})
        self.fields['empresa_nome'].widget.attrs.update({'class': 'select form-control'})
        self.fields['caminhao_placa'].widget.attrs.update({'class': 'select form-control'})
        self.fields['quant_retiradas'].widget.attrs.update({'class': 'form-control'})
        self.fields['cartao_numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['peso_vazio'].widget.attrs.update({'class': 'form-control'})
        self.fields['peso_carregado'].widget.attrs.update({'class': 'form-control'})
        self.fields['material'].queryset = Material.objects.filter(tipo='Coleta')

        if 'empresa' in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                print(empresa_id)
                self.fields['motorista_cpf'].queryset = Motorista.objects.filter(empresa_id=empresa_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # self.fields['motorista_cpf'].queryset = self.instance.empresa_nome.motorista_cpf_set
            # Quando faz edição perde funcionalidade de filtro
            self.fields['motorista_cpf'].queryset = Motorista.objects.all()

        if 'empresa' in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                self.fields['caminhao_placa'].queryset = Caminhao.objects.filter(empresa_id=empresa_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # self.fields['caminhao_placa'].queryset = self.instance.empresa_nome.caminhao_placa_set
            # Quando faz edição perde funcionalidade de filtro
            self.fields['caminhao_placa'].queryset = Caminhao.objects.all()


class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = '__all__'
        exclude = ['usuario', 'peso_carga', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['motorista_cpf'].widget.attrs.update({'class': 'select form-control'})
        self.fields['empresa_nome'].widget.attrs.update({'class': 'select form-control'})
        self.fields['caminhao_placa'].widget.attrs.update({'class': 'select form-control'})
        self.fields['material'].widget.attrs.update({'class': 'select form-control'})
        self.fields['cartao_numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['peso_vazio'].widget.attrs.update({'class': 'form-control'})
        self.fields['peso_carregado'].widget.attrs.update({'class': 'form-control'})
        self.fields['material'].queryset = Material.objects.filter(tipo='Entrega')

        if 'empresa' in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                print(empresa_id)
                self.fields['motorista_cpf'].queryset = Motorista.objects.filter(empresa_id=empresa_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # self.fields['motorista_cpf'].queryset = self.instance.empresa_nome.motorista_cpf_set
            # Quando faz edição perde funcionalidade de filtro
            self.fields['motorista_cpf'].queryset = Motorista.objects.all()

        if 'empresa' in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                self.fields['caminhao_placa'].queryset = Caminhao.objects.filter(empresa_id=empresa_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            # self.fields['caminhao_placa'].queryset = self.instance.empresa_nome.caminhao_placa_set
            # Quando faz edição perde funcionalidade de filtro
            self.fields['caminhao_placa'].queryset = Caminhao.objects.all()
