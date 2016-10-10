from flask_restful import Resource
from flask import request
from postgresdb.models import Usuario
from postgresdb.repository.UsuarioRepository import UsuarioRepository

class UsuarioRest(Resource):

    def post(self):
        
        usuarioRepository = UsuarioRepository()

        usuarioInsert = Usuario(usuarioRequest['usuario'], usuarioRequest['clave'], usuarioRequest['correo'])
        usuarioRepository.insertar(usuarioInsert)
        
        return {'response': 'Correct!!'}