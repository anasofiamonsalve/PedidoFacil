from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)   # inicia sesión automáticamente
            messages.success(request, '¡Cuenta creada! Bienvenido a PedidoFácil.')
            return redirect('lista_productos')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})