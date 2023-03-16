from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.tarea_model import Tarea
from bd import conexion

class TareasController(Resource):
    @jwt_required()
    def post(self):
        usuario_id = get_jwt_identity()
        data = request.json
        

    def get(self):
        pass
