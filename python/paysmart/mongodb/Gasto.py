import os

from mongodb.Conexion import Conexion
from util.Constantes import Constantes

class Gasto:

    conexionDB = None

    #INSERTAR
    def insert(self, document):
        conexion = Conexion.getConexion()
        db = conexion.test
        result = db.gastos.insert_one(document)
        print(result)
        return result

    #INSERTAR DE FORMA MASIVA
    def insertMasive(self, collectionName):
        os.system("mongoimport --db test --collection "+collectionName+" --file "+Constantes.FILE_OUTPUT_JSON)
