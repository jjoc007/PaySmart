from flask_restful import Resource
from flask import request
from postgresdb.models import SubCategoria
from postgresdb.Conexion import Conexion

class SubCategoriaRest(Resource):
    
    def get(self):

        Conexion.getConexion()
        session = Conexion.session

        cat1 = SubCategoria('IMPUESTOS',35)
        cat2 = SubCategoria('VECA',36)
        session.add(cat1)
        session.add(cat2)
        session.commit()

        return {'hello': 'Juan Jose'}

    def post(self):
        
        return {'hola': 'mundo'}

    def options(self):
        return ""