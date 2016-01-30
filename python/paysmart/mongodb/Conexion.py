import sys

from pymongo import MongoClient
from pymongo.errors import  ConnectionFailure

from util.Constantes import Constantes

class Conexion:

    @staticmethod
    def getConexion():

        try:
            conectorMongo = MongoClient("mongodb://"+Constantes.DB_HOST+":"+Constantes.DB_PORT)
            print("Conectado a Mongo !!")
        except ConnectionFailure, e:
            sys.stderr.write("no se conecto: %s" % e)
        return conectorMongo

