from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EditarClaveForm

from django.contrib.auth.hashers import make_password

@login_required
def index_view(request):
    return render(request, 'usuario/index.html')


def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('usuario.index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('usuario.index'))
            else:
                mensaje = 'Cuenta inactiva'
        mensaje = 'Nombre de usuario o clave no valido'
    return render(request, 'usuario/login.html', {'mensaje': mensaje})

def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado con exito')
	return redirect(reverse('usuario.login')) 

@login_required
def editar_clave_view(request):
    if request.method == 'POST':
        form = EditarClaveForm(request.POST)
        if form.is_valid():
            request.user.password = make_password(form.cleaned_data['password'])
            request.user.save()
            messages.success(request, 'Su clave ha sido cambiada con exito...!')
            messages.success(request, 'Es necesario introducir los datos para entrar...!')
            return redirect(reverse('usuario.index'))
    else:
        form = EditarClaveForm()
    return render(request,'usuario/editar_contrasena.html',{'form' : form})