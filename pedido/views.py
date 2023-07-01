from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def infopedido(request):
    return render(request, 'info-pedido.html')
