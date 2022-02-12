from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random


class Animal(BaseModel):
    nome: str
    idade: int
    sexo: str
    cor: str


app = FastAPI()

origins = [
    "http://0.0.0.0:5500"
]

BD = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return "Olá, vá para o endpoint http://localhost:8000/docs"


@app.get("/animais")
def showAnimals():
    return BD


@app.post("/animais")
def insertAnimals(animal: Animal):
    animal_dict = animal.dict()
    if animal.sexo in ['macho', 'femea']:
        animal_dict['id'] = str(random.randint(1, 10000))
        BD.append(animal_dict)
        return f'O animal {animal.nome} foi inserido com sucesso!'
    else:
        return f'O animal inserido está com o campo "sexo" errado... Corrija antes de fazer a inserção!'


@app.get("/animais/{id}")
def findAnimal(id):
    r = [l for l in BD if l["id"] == str(id)]
    return r if r != [] else {'erro': f'Id[{id}] não existe!'}


@app.delete("/animais/{id}")
def deleteAnimal(id):
    try:
        index = [i for i, l in enumerate(BD) if l['id'] == str(id)][0]
        del BD[index]
        return {'mensagem': f'O {id} foi apagado'}
    except IndexError:
        return {'error': 'O animal não foi encontrado!'}
