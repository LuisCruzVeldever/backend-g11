from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models.producto_model import Producto
from dtos.categoria_dto import CategoriaDto

class ProductoDto(SQLAlchemyAutoSchema):
    class Meta : 
        # Sirve para indicar a mi DTO que ahora queremos que tambien reconozca los columnas que sean FK
        incluido_fk = True
        model = Producto