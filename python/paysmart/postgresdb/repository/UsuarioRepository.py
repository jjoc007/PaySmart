from postgresdb.models import Usuario
from postgresdb.Conexion import Conexion

class UsuarioRepository:

	def __init__(self):
		Conexion.getConexion()

	def insertar(self, usuario):
		session = Conexion.session
		session.add(usuario)
		session.commit()

	def autenticar(self, nombreUsuario, clave):
		session = Conexion.session
		query = session.query(Usuario).filter(Usuario.usuario==nombreUsuario).filter(Usuario.clave==clave)
		return query.first()