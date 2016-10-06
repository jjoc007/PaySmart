from flask_restful import Resource
from flask import request
from mongodb.Gasto import Gasto

class GastoRest(Resource):

    def post(self):
        print(request)
        print(request.json['gasto'])

        gasto= Gasto()
        gasto.insert(request.json['gasto'])

        return {'hola': 'mundo'}
