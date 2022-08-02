from http.client import HTTPResponse
from operator import truediv
import time
from types import NoneType
from django.shortcuts import render, redirect
from .models import login_senha
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import decorators
# Create your views here.


def paginateste(request):
    # form=UserCreationForm()
    # context={'user_data': login_senha.objects.all().values,
    #     'formulario': form}
    # if request.method == 'POST':
    #     form=UserCreationForm(request.POST)
    #     form.save()
    context={'mensagem': ''}
    if request.method == 'POST':
        _var_nome = request.POST.get('nome', None)
        _var_senha=None
        tried=False
        senha_invalid=False
        try:

            _var_senha = int(request.POST.get('senha', None))
        
        except:
            context['mensagem']='Não é possível criar uma senha com letras ou caracteres especiais'
            senha_invalid=True
            
        
        finally:        
            senhas_proibidas=['1234',
                                    '10203',  '12345', '123456', '1234567',
                                    '12345678',
                                    '123456789',
                                    '1234567890',
                                    '9876543210',
                                    '987654321',
                                    '87654321',
                                    '7654321',
                                    '654321',
                                    '54321',
                                    '000000',
                                    '111111',
                                    '999999',
                                    '555555',
                                    '102030',
                                    '123123',
                                    'abc123',
                                    '1q2w3e4r',
                                    'q1w2e3r4t5y6',
                                    'senha',
                                    'Brasil',
                                    'qwerty',
                                    'password',]
            if senha_invalid:
                context['mensagem']='Credencial não pode ser nula ou conter letras e caracteres especiais'
            elif str(_var_senha) not in senhas_proibidas and len(str(_var_senha))>4:
                login_senha.objects.create(username=_var_nome, password=_var_senha)
                return redirect('home')
            
            else:
                context['mensagem']='Sua senha apresenta uma segurança baixa.'

        
    return render(request, 'teste.html', context)

def pagina_home(request):
    var = request.session.get('username')
    var2=request.session.get('senha')
    redirect_not= False
    for x in login_senha.objects.all():
        if x.username == var and str(x.password) == var2:

            redirect_not=True
            return render(request, 'home.html')
        

    if not redirect_not:
        redirect('login')

    
    



def pagina_login(request):
    context={'mensagem_login': 'Preencha as credenciais'}
    if request.method == 'POST':
        _var_nome = request.POST.get('nome', None)
        _var_senha = int(request.POST.get('senha', None))
        not_logged_in=True
        for x in login_senha.objects.all():
            
            if (_var_nome == x.username and _var_senha == x.password):
                print('ok')
                context['mensagem_login']='CREDENCIAIS certas'
                time.sleep(3)
                request.session["username"] = x.username
                request.session['senha'] =str(x.password)
                return redirect('home')
            
        if   not_logged_in:
            context['mensagem_login']='CREDENCIAIS ERRADAS!!!'
            

            
    return render(request, 'login.html', context)