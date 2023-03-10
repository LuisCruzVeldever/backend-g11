from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.nivel_model import Nivel

class NivelCto(SQLAlchemyAutoSchema):
    class Meta:
        # model > para imndicar que modelo tiene que utilizar para poder hacer el mapeo y validaciones de los atributos
        model = Nivel