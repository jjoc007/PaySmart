from flask_restful import Resource
from flask import request
from postgresdb.models import SubCategoria
from postgresdb.Conexion import Conexion

class SubCategoriaRest(Resource):
    
    def post(self):
        
        Conexion.getConexion()
        session = Conexion.session
        categoriaRequest = request.json['subCategoria']

        subCategoriaDao = SubCategoria(categoriaRequest['descripcion'], categoriaRequest['idCategoria'])
        session.add(subCategoriaDao)
        session.commit()        

        return {'response': 'Correct!!'}