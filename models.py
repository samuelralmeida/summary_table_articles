from sqlalchemy import Column, Integer, String
from database import Base

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(50), default=None)
    autor = Column(String(50), default=None)
    ano = Column(Integer(10), default=None)
    local = Column(String(50), default=None)
    objetivos = Column(String(750), default=None)
    delineamento = Column(String(750), default=None)
    discussao = Column(String(750), default=None)
    desfecho = Column(String(750), default=None)
    resultados = Column(String(750), default=None)

    @property
    def serialize(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano,
            'local': self.local,
            'objetivos': self.objetivos,
            'delineamento': self.delineamento,
            'discussao': self.discussao,
            'desfecho': self.desfecho,
            'resultados': self.resultados
        }
