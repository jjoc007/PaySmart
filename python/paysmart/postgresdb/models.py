import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String())
    subCategorias = relationship("SubCategoria")

    def __init__(self, descripcion):
        self.descripcion = descripcion
        
    def __repr__(self):
        return '<id {}>'.format(self.id)

class SubCategoria(Base):
    __tablename__ = 'sub_categoria'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String())
    categoriaId = Column('categoria_id',Integer, ForeignKey('categoria.id'))

    def __init__(self, descripcion, categoriaId):
        self.descripcion = descripcion
        self.categoriaId = categoriaId
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
