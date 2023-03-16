from flask_restful import Resource, request
from flask_jwt_extend import jwt_required, get_jwt_identity

from models.tarea_model import Tarea
from bd import conexion

class TareasController(Resource):
    def post(self):
        pass
    def get(self):
        pass
