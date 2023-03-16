from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from controllers.usuario_controller import UsuariosController, LoginController, PerfilController

from bd import conexion

app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:.1624soporte@localhost:5432/tareas'
# Variable de la configuracionpara JWT
app.config['JWT_SECRET_KEY'] = 'ultrasupersecreto'
#estamos modificando el tiempo de expiracion en 1 hora y 10 minutos
app.config['JWT_Access_TOKEN_EXPIRES'] = timedelta(hours=1,minutos=10)

api = Api(app)
conexion.init_app(app)

Migrate(app = app,db = conexion)
JWTManager(app)

#definir mis rutas del proyecto

api.add_resource(UsuariosController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(PerfilController, '/perfil')


if  __name__ == '__main__':
    app.run(debug=True)