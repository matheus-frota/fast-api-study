from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import criar_bd, get_db
from src.infra.sqlalchemy.repositorios.serie import RepositorioSerie
from src.schemas.schemas import Serie as schema_serie


criar_bd()


app = FastAPI()


@app.post('/series')
def inserir_serie(serie: schema_serie, db: Session=Depends(get_db)):
    RepositorioSerie(db).criar(serie)
    return {'msg': f'A serie [{serie.titulo}] foi inserida no DB.'}


@app.get('/series')
def listar_todos(db: Session=Depends(get_db)):
    return RepositorioSerie(db).listar()


@app.get('/series/{serie_id}')
def listar_por_id(serie_id: int, db: Session=Depends(get_db)):
    return RepositorioSerie(db).selecionar_id(serie_id)


@app.delete('/series/{serie_id}')
def remover_serie(serie_id: int, db: Session=Depends(get_db)):
    RepositorioSerie(db).remover_serie(serie_id)
    return {'msg': 'Serie removida com sucesso!'}
