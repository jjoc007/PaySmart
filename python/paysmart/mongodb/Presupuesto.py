import os

from mongodb.Conexion import Conexion
from util.Constantes import Constantes

class Presupuesto:

    conexionDB = None

    #INSERTAR
    def insert(self, document):
        conexion = Conexion.getConexion()
        db = conexion.test
        result = db.presupuestos.insert_one(document)
        print(result)
        return result

    #CONSULTAR TODOS
    def getAll(self):
		conexion = Conexion.getConexion()
		db = conexion.test
		result = db.presupuestos.find()
		return result
