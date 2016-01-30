import os

from mongodb.Conexion import Conexion
from util.Constantes import Constantes


class LoadDataAnalitic:

    conexionDB = None

    #CRUD BASICO DE MONGO CON LAS COLECCIONES DE CARGUE DE INFORMACION A ANALIZAR

    #INSERTAR
    def insert(self, document, collectionName):
        pass

    #UPDATE
    def update(self, document, idDocument, collectionName):
        pass


    #DELETE
    def delete(self, idDocument, collectionName):
        pass

    #INSERTAR DE FORMA MASIVA
    def insertMasive(self, collectionName):
        os.system("mongoimport --db test --collection "+collectionName+" --file "+Constantes.FILE_OUTPUT_JSON)

    #CONSULTAR BY ID
    def queryById(self, idDocument, collectionName):
        pass


    #CONSULTAR COMPLETAMENTE
    def queryAll(self, collectionName):
        pass