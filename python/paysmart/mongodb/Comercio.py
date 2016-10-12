import os

from mongodb.Conexion import Conexion
from util.Constantes import Constantes

class Comercio:

    conexionDB = None

    #INSERTAR
    def insert(self, document):
        conexion = Conexion.getConexion()
        db = conexion.test
        result = db.comercios.insert_one(document)
        print(result)
        return result

	#CONSULTAR TODOS
	def getAll(self):
		conexion = Conexion.getConexion()
		db = conexion.test
		result = db.comercios.find()
		return result