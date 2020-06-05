from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from contas.forms import CriarUsuarioForm, EditarContaForm


def login_usuario(request):
    return render(request, 'registration/login.html')


@login_required(login_url='/login/')
def logout_usuario(request):
    logout(request)
    return redirect('/login/')


@csrf_protect
def login_submit(request):
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('/')
        else:
            messages.error(request, ' Usuário e/ou senha inválidos. Favor tentar novamente!')
    return redirect('/login/')


def criar_usuario(request):
    template_name = 'registration/criar_usuario.html'
    if request.POST:
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('/')
    else:
        form = CriarUsuarioForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def painel_controle(request):
    template_name = 'painel.html'
    return render(request, template_name)


@csrf_protect
@login_required(login_url='/login/')
def editar(request):
    template_name = 'registration/editar.html'
    context = {}
    form = EditarContaForm(request.POST or None, instance=request.user)
    if request.POST:
        form = EditarContaForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarContaForm(instance=request.user)
            context['sucess'] = True
            messages.success(request, 'Dados alterados com sucesso!')
            return redirect('/')
        else:
            form = EditarContaForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@csrf_protect
@login_required(login_url='/login/')
def editar_senha(request):
    template_name = 'registration/editar_senha.html'
    context = {}
    if request.POST:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['sucess'] = True
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

