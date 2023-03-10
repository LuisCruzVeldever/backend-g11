from base_de_datos import conexion
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey

class Seccion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    alumnos = Column(type_=types.Integer, default=10)

    #si una columna serautilizadas como llave foranea entonces tenemos que utilizar la claee ForeignKey, en ella usaremos el parametro 'column' en el cual indicamremos LA TABLA

    nivelid = Column(ForeignKey(column='niveles.id'), type_=types.Integer,
    nullable=False, name='nivel_id')

    maestroId = Column(ForeignKey(column='maestro.id'), type_=types.Integer,
                       nullable=False, name='maestro_id')
                       
                       

    __tablename__ = 'secciones'