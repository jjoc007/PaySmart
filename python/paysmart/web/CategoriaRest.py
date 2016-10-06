from flask_restful import Resource
from flask import request
from postgresdb.models import Categoria
from postgresdb.Conexion import Conexion

class CategoriaRest(Resource):

    def post(self):
        
        Conexion.getConexion()
        session = Conexion.session
        categoriaRequest = request.json['categoria']

        categoriaDao = Categoria(categoriaRequest['descripcion'])
        session.add(categoriaDao)
        session.commit()        

        return {'response': 'Correct!!'}