from flask import Flask
from flask_cors.extension import CORS
from flask_restful import Api
from web.GastoRest import GastoRest


app = Flask(__name__)
cors = CORS(app)
api = Api(app)

api.add_resource(GastoRest, '/Gasto',endpoint='Gasto')


if __name__ == "__main__":
    app.run(debug=True)