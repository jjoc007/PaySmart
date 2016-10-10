from postgresdb.repository.UsuarioRepository import UsuarioRepository

class JwtUtils:

	@staticmethod
	def authenticate(username, password):

		#CONSULTAR USUARIO Y CLAVE
		usuarioRepository = UsuarioRepository()
		usuario = usuarioRepository.autenticar(username,password)

		print usuario

		if usuario:
			return usuario

	@staticmethod
	def identity(payload):
		user_id = payload['identity']
		return user_id