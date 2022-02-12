from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import criar_db, get_db

criar_db()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):
    return RepositorioProduto(db).listar()
