
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Sistema de Controle de Estoque"}

@app.post("/insumos/", response_model=schemas.Insumo)
def create_insumo(insumo: schemas.InsumoCreate, db: Session = Depends(get_db)):
    return crud.create_insumo(db=db, insumo=insumo)

@app.get("/insumos/", response_model=list[schemas.Insumo])
def read_insumos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    insumos = crud.get_insumos(db, skip=skip, limit=limit)
    return insumos

@app.get("/insumos/{insumo_id}", response_model=schemas.Insumo)
def read_insumo(insumo_id: int, db: Session = Depends(get_db)):
    db_insumo = crud.get_insumo(db, insumo_id=insumo_id)
    if db_insumo is None:
        raise HTTPException(status_code=404, detail="Insumo not found")
    return db_insumo
