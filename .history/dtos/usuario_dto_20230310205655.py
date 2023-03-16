from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from models.usuario_model import Usuario


class UsuarioDto(SQLAlchemyAutoSchema):
        model=Usuario

class LoginDto(Schema):
    #Validar el siguiente patron (expresion regular) xxxxx@xxxx
    correo = fields.Email(required=True, error_messages={'required': 'El correo debe ser requerido'})
    password = fields.Str(required=True, error_messages={'required': 'El password  debe ser requerido'})