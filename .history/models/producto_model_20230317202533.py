from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
from db import conexion

class Producto(conexio.Model):
    id=Column(types.Integer, primary_key=True, autoincrement=True) 
    nombre = Column(type_=types.Text, nullable=False) 
    precio = Column(type_=types.Float )
    imagen = Column(type_=types.Text)
    categoriaId = Column(ForeignKey('categorias.id'), type_=types.Integer, nullable=False, name='categoria_id') 
    

    created_at = Column(type_=types.DateTime, default=datetime.utcnow, name='createAt')   ## utc entonces es la zona horaria de datetime  ###UTF es la forma

    __tablename__ = 'productos'