from flask_restful import Resource
from flask import request
from postgresdb.models import Categoria
from postgresdb.Conexion import Conexion

class CategoriaRest(Resource):
    def get(self):

        Conexion.getConexion()
        session = Conexion.session

        # Insert a Person in the person table
        cat1 = Categoria('IMPUESTOS')
        cat2 = Categoria('VECA')
        session.add(cat1)
        session.add(cat2)
        session.commit()

        return {'hello': 'Juan Jose'}

    def post(self):
        
        return {'hola': 'mundo'}

    def options(self):
        return ""