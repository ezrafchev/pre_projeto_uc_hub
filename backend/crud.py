
from sqlalchemy.orm import Session
from . import models, schemas

def get_insumo(db: Session, insumo_id: int):
    return db.query(models.Insumo).filter(models.Insumo.id == insumo_id).first()

def get_insumos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Insumo).offset(skip).limit(limit).all()

def create_insumo(db: Session, insumo: schemas.InsumoCreate):
    db_insumo = models.Insumo(nome=insumo.nome, quantidade=insumo.quantidade, preco=insumo.preco)
    db.add(db_insumo)
    db.commit()
    db.refresh(db_insumo)
    return db_insumo
