from flask import Flask
from flask_cors.extension import CORS
from flask_restful import Api
from web.GastoRest import GastoRest 
from web.CategoriaRest  import CategoriaRest
from web.SubCategoriaRest  import SubCategoriaRest

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

#SERVICIOS
api.add_resource(GastoRest, '/Gasto',endpoint='Gasto')
api.add_resource(CategoriaRest, '/Categoria',endpoint='Categoria')
api.add_resource(SubCategoriaRest, '/SubCategoria',endpoint='SubCategoria')

if __name__ == "__main__":
    app.run(debug=True)
    