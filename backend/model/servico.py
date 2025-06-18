from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base

class ServicoResponse(BaseModel):
    id: int
    cliente: str
    tatuador: str
    status: str

    class Config:
        orm_mode = True

class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    tatuador = Column(String, nullable=False)
    status = Column(String, nullable=False)