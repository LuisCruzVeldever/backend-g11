from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import Schema, fields
from models.usuario_model import Usuario


class UsuarioDto(SQLAlchemyAutoSchema):
    #podemos utilizar la funcion auto_field para generar un Field de marshmallow basado en el modelo que estamos indicando, osea esto modificara la configuracion del atributo
    #https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Field
    #load_only > solamente este campo sera necesario para cuando queramos validar la infromacion entrante,
    #pero si queremos devolver informacio esta campo se omitira
    password = auto_field(load_only=True)
    class Meta:
        model=Usuario

class LoginDto(Schema):
    #Validar el siguiente patron (expresion regular) xxxxx@xxxx
    correo = fields.Email(required=True, error_messages={'required': 'El correo debe ser requerido'})
    password = fields.Str(required=True, error_messages={'required': 'El password  debe ser requerido'})