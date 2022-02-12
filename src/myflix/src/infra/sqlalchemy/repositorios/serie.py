from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioSerie():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Serie):
        db_serie = models.Serie(
            titulo=produto.titulo,
            ano=produto.ano,
            genero=produto.genero,
            qtd_temporadas=produto.qtd_temporadas
        )

        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def listar(self):
        return self.db.query(models.Serie).all()

    def selecionar_id(self, serie_id: int):
        stmt = select(models.Serie).filter_by(id=serie_id)
        return self.db.execute(stmt).one()

    def remover_serie(self, serie_id: int):
        stmt = delete(models.Serie).where(models.Serie.id == serie_id)

        self.db.execute(stmt)
        self.db.commit()
