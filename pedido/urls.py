from django.urls import path
from pedido.views import index, infopedido

urlpatterns = [
    path('', index),
    path('info-pedido/', infopedido, name='info-pedido'),
]
