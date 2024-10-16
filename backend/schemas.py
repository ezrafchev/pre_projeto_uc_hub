
from pydantic import BaseModel

class InsumoBase(BaseModel):
    nome: str
    quantidade: int
    preco: float

class InsumoCreate(InsumoBase):
    pass

class Insumo(InsumoBase):
    id: int

    class Config:
        orm_mode = True
