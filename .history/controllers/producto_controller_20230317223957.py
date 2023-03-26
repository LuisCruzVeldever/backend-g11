from flask_restful import Resource, request
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto

class ProductController(Resource):
    def post(self):
        data = request.form
        imagen = request.files.get('imagen')
        data['images'] = imagen.filename
        try:
            dto = ProductoDto()
            data_serializada = dto.load(data)
            return {
                'message': 'Producto creado exitosamente'
                }
        except Exception as error:
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        