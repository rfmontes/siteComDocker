from django import forms

from cadastros.models import Motorista, Caminhao, Empresa, Material, Grupo


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'
        exclude = ['usuario', ]

    def clean_nome_completo(self):
        nome = self.cleaned_data.get('nome_completo')
        if any(char.isdigit() for char in nome):
            raise forms.ValidationError('Caractere inválido!')
        else:
            return nome

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria_cnh'].widget.attrs.update({'class': 'select form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome_completo'].widget.attrs.update({'class': 'form-control'})
        self.fields['cnh'].widget.attrs.update({'class': 'form-control'})
        self.fields['empresa'].widget.attrs.update({'class': 'select form-control'})


class CaminhaoForm(forms.ModelForm):
    class Meta:
        model = Caminhao
        fields = '__all__'
        exclude = ['usuario', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['placa'].widget.attrs.update({'class': 'form-control'})
        self.fields['marca'].widget.attrs.update({'class': 'form-control'})
        self.fields['modelo'].widget.attrs.update({'class': 'form-control'})
        self.fields['cor'].widget.attrs.update({'class': 'form-control'})
        self.fields['empresa'].widget.attrs.update({'class': 'select form-control'})


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = ['usuario', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['uf'].widget.attrs.update({'class': 'select form-control'})
        self.fields['nome_empresa'].widget.attrs.update({'class': 'form-control'})
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['bairro'].widget.attrs.update({'class': 'form-control'})
        self.fields['cidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['responsavel'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefone1'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefone2'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_atuacao'].widget.attrs.update({'class': 'form-control'})


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = ['usuario', 'minha_ordem', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_grupo'].widget.attrs.update({'class': 'select form-control'})
        self.fields['tipo'].widget.attrs.update({'class': 'select form-control'})
        self.fields['nome_material'].widget.attrs.update({'class': 'form-control'})
        self.fields['preco_material'].widget.attrs.update({'class': 'form-control'})


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        exclude = ['usuario', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_grupo'].widget.attrs.update({'class': 'form-control'})
        self.fields['preco_grupo'].widget.attrs.update({'class': 'form-control'})
