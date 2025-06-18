from sqlalchemy.orm import Session
from model.servico import Servico

class ServicoService:
    def __init__(self, db: Session):
        self.db = db

    def listar_servicos(self):
        return self.db.query(Servico).all()
