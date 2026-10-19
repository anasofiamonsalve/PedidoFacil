from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Pedido
from .forms import PedidoForm


@login_required
def lista_pedidos(request):
    q = request.GET.get('q', '')
    pedidos = Pedido.objects.select_related('usuario').order_by('-fecha_registro')
    if q:
        pedidos = pedidos.filter(cliente__icontains=q)
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos, 'q': q})


@login_required
def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedidos/detalle.html', {
        'pedido': pedido,
        'estados': Pedido.ESTADOS,
    })


@login_required
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user    
            pedido.save()
            messages.success(request, 'Pedido registrado correctamente.')
            return redirect('lista_pedidos')
        messages.error(request, 'Revisa los errores del formulario.')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/form.html', {'form': form, 'titulo': 'Nuevo pedido'})


@login_required
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido actualizado correctamente.')
            return redirect('lista_pedidos')
        messages.error(request, 'Revisa los errores del formulario.')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/form.html', {'form': form, 'titulo': 'Editar pedido'})


@login_required
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado correctamente.')
        return redirect('lista_pedidos')
    return render(request, 'pedidos/confirmar_eliminar.html', {'pedido': pedido})


@login_required
@require_POST
def cambiar_estado(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    nuevo_estado = request.POST.get('estado')
    estados_validos = [valor for valor, nombre in Pedido.ESTADOS]
    if nuevo_estado in estados_validos:
        pedido.estado = nuevo_estado
        pedido.save()
        messages.success(request, f'Estado cambiado a "{pedido.get_estado_display()}".')
    else:
        messages.error(request, 'Estado no válido.')
    return redirect('detalle_pedido', pk=pk)