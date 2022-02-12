# App BLX

App para anúncio e vendas de produtos na vizinhança.

## Funcionalidades

* Qualquer pessoa poderá anunciar produtos;
* Qualquer pessoa poderá fazer pedidos dos produtos;
* Uma pessoa tem:
  * Nome
  * Telefone
  * Senha(?)

* Um produto tem:
  * Nome
  * Detalhamento
  * Preço
  * Disponibilidade
  * Fotos

* Um Pedido tem:
  * Produto
  * Pessoa que está pedindo
  * Pessoa que está vendendo
  * Quantidade
  * Local de entrega[
  * Tipo de envio: Entrega ou retirada no local
  * Observações

* Cada usuário terá uma lista de pedidos recebidos (Vendas) e pedidos feitos (Compras)
* O pedido deverá ser aceito pelo vendedor
* O comprador poderá acompanhar seus pedidos
  * Status(Feito, Aceito, Entregue)

## Arquitetura

* Python + FastAPI
* API REST
* Banco de dados: MySQL e/ou MongoDB
* Docker para os bancos de dados
* MVC
* Domain Drive Design e Arquitetura limpa