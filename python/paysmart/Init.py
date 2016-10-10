from flask import Flask
from flask_cors.extension import CORS
from flask_restful import Api
from flask_jwt import JWT, current_identity
from werkzeug.security import safe_str_cmp

from web.JwtUtils import JwtUtils 

from web.GastoRest import GastoRest 
from web.CategoriaRest  import CategoriaRest
from web.SubCategoriaRest  import SubCategoriaRest
from web.ComercioRest  import ComercioRest
from web.UsuarioRest  import UsuarioRest

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super-secret'

cors = CORS(app)
api = Api(app)
jwt = JWT(app, JwtUtils.authenticate, JwtUtils.identity)

#SERVICIOS
api.add_resource(GastoRest, '/Gasto',endpoint='Gasto')
api.add_resource(ComercioRest, '/Comercio',endpoint='Comercio')

api.add_resource(CategoriaRest, '/Categoria',endpoint='Categoria')
api.add_resource(SubCategoriaRest, '/SubCategoria',endpoint='SubCategoria')
api.add_resource(UsuarioRest, '/Usuario',endpoint='Usuario')

if __name__ == "__main__":
    app.run(debug=True)
    