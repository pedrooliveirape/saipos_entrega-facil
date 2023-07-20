from pathlib import Path, os
from dotenv import load_dotenv
from django.shortcuts import render
from funcoes.buscar_pedido import pedido_info, abrir_entregaFacil
from pedido.forms import PedidoForms

def index(request):
    return render(request, 'index.html')

def infopedido(request):
    auth_saipos = str(os.getenv('auth_saipos'))
    if 'inputpedido' in request.GET:
        numero_pedido = request.GET['inputpedido']        

    infos_pedido = pedido_info(auth=auth_saipos, num_pedido=numero_pedido)
    form = PedidoForms(infos_pedido)

    if request.method == 'POST':
        form = PedidoForms(request.POST)
        if form.is_valid():
            abrir_entregaFacil(form)
            return render(request, 'index.html')

    return render(request, 'info-pedido.html', {'form': form})
