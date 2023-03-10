from base_de_datos import conexion
from sqlalchemy import Column, types

#Las tablas se van a comportar como si fueran clases y un atrubuto de la clase
class Nivel(conexion.Model):
    # https://docs.sqlalchemist
    id= Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nuemro=Column(type_=types.Integer, nullable=False, unique=True)
    descripcion = Column(type_=types.Text)

    # como se llamara la tabla en la base de datos
    __tablename__ = 'niveles'