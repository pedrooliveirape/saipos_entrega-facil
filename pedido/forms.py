from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList

class PedidoForms(forms.Form):
    numero_pedido = forms.CharField(
        label='Número do pedido',
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    nome_cliente = forms.CharField(
        label='Nome do cliente',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    telefone = forms.CharField(
        label='Telefone',
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    data = forms.CharField(
        label='Data',
        required=True,
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    endereco_entrega = forms.CharField(
        label='Endereço de entrega',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    numero_entrega = forms.CharField(
        label='Número',
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    complemento = forms.CharField(
        label='Complemento',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    referencia = forms.CharField(
        label='Ponto de referência',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    valor_produtos = forms.FloatField(
        label='Valor de produtos',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    frete = forms.FloatField(
        label='Valor do frete',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    total_pedido = forms.FloatField(
        label='Valor do pedido',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    forma_pagamento = forms.CharField(
        label='Forma de Pagamento',
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    pagamento_entrega = forms.BooleanField(
        required=False,
        label='Solicitar pagamento na entrega',
        widget=forms.CheckboxInput(
            attrs={
                '': '',
                'class': 'form-check-input',
                'type': 'checkbox'
            }
        )
    )
