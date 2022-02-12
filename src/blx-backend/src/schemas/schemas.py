from typing import List, Optional

from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
#     meus_produtos: List[Produto]
#     vendas: List[Pedido]
#     pedidos: List[Pedido]


class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Condig:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario_vendedor: Usuario
    usuario_comprador: Usuario
    produto: Produto
    quantidade: int
    local: str
    envio: str
    observacao: Optional[str] = ''
