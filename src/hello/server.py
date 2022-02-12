from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    name: str
    price: float


app = FastAPI()


@app.get("/hello/{nome}")
def home(nome):
    # Aplicação: método HTTP - ENDPOINT ou ROTA ou PATH
    # O que são rotas
    # O que são métodos HTTP
    text = f'Hello {nome}! /n How are you???'
    return {'menssage': text}


@app.get("/calc/{value}")
def calc(value: int) -> dict:
    # Exemplo de parâmetro de Rota/Path -> localhost/calc/10
    return {'menssage': f'Square number is {value**2}'}


@app.get("/double")
def double(value: int):
    # Exemplo de parâmetro de query -> localhost/double?value=10
    return {'menssage': f'{value**2}'}


@app.post('/produtos')
def products(produto: Produto):
    return {
        'menssage':
        f'Produto ({produto.name} - R${produto.price}) cadastrado com sucesso!'
    }
