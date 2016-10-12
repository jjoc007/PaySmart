from flask_restful import Resource
from flask import request
from mongodb.Presupuesto import Presupuesto

class PresupuestoRest(Resource):

    def post(self):
        presupuesto= Presupuesto()
        presupuesto.insert(request.json['presupuesto'])

        return {'hola': 'mundo'}