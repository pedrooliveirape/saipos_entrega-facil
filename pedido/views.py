from pathlib import Path, os
from dotenv import load_dotenv
from django.shortcuts import render
from funcoes.buscar_pedido import pedido_info


def index(request):
    return render(request, 'index.html')

def infopedido(request):
    auth_saipos = str(os.getenv('auth_saipos'))
    if 'inputpedido' in request.GET:
        numero_pedido = request.GET['inputpedido']

    infos_pedido = pedido_info(auth=auth_saipos, num_pedido=numero_pedido)
    
    return render(request, 'info-pedido.html', {'itens': infos_pedido})
