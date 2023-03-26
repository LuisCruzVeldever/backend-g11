from flask_restful import Resource, request
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto
from os import path

class ProductosController(Resource):
    def post(self):
        data = request.form.to_dict()
        # TODO: validar que tengamos esa llave en el formulario llamada 'imagen'
        # TODO: VALIDAR QUE SOLO SEAN IMAGENES
        imagen = request.files.get('imagen')
        #TODO: agregar un uuid al nombre de la imagen
        data['images'] = imagen.filename
        try:

            dto = ProductoDto()
            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)

            conexion.session.add(nuevo_producto)
            imagen.save(path.join('images', data[imagen]))

            conexion.session.commit()
            return {
                'message': 'Producto creado exitosamente'
                }
        except Exception as error:
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        
    def get (self):
        resultado = conexion.session.query(Producto).all
        