from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CriarUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    # verifica se ja existe email cadastrado
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail cadastrado!')
        return email

    # Método para tambem salvar o email do usuario
    def save(self, commit=True):
        user = super(CriarUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EditarContaForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail cadastrado!')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


