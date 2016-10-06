from flask_restful import Resource
from flask import request
from mongodb.Comercio import Comercio

class GastoRest(Resource):

    def post(self):
        print(request)
        print(request.json['comercio'])

        comercio= Comercio()
        comercio.insert(request.json['comercio'])

        return {'hola': 'mundo'}
