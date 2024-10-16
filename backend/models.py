
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Insumo(Base):
    __tablename__ = "insumos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    quantidade = Column(Integer)
    preco = Column(Float)
