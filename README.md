# API Pedidos

Repositório do projeto de integração via API e bot dos pedidos realizados no sistema Saipos com o Entrega Fácil do Ifood.

## Contextualização do problema

O Delivery cliente utiliza o sistema de gestão Saipos, tanto para gerir pedidos recebidos, como para fazer a gestão administrativa e também utiliza o serviço entrega fácil do Ifood para solicitar motoqueiros para realizar algumas das suas entregas.

O problema é que eles perdem muito tempo passando as informações manualmente do sistema saipos para a tela de solicitação de entregador no portal do Ifood.

## Solução

A solução é construir uma página simples que receba o id do pedido no sistema Saipos e preencha a um apertar de botão as informações de entrega na do Entrega fácil no site do Ifood. 

Para isso utilizarei o Python com o framework Django, o bootstrap para ajudar na criação da página. Acessarei o sistema saipos a partir das suas APIs escondidadas para solicitar os pedidos e pretendo empurrar as informações ao Ifood através do selenium do Python.

## Lista de tarefas

- [x] Criar página html com Bootstrap
- [x] Renderizar a página com Django
- [x] Criar função de acessar a API de pedido na Saipos
- [ ] Criar função de enviar pedido para o Entrega Fácil
- [ ] Automatizar a autenticação 