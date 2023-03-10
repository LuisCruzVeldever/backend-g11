from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto



class NivelController(Resource):
    #GET, POST, PUT, DELETE
    def get(self):
        query : Query = conexion.session.query(Nivel)
        # SELECT * FROM niveles;
        resultado = query.all()

        dto = NivelDto()
        # dump > es un metod en el cual le paso la/las instancias que quiero convertir a tipos de adtos genericos . Si se le pasa mas de una instancia, osea una lista 
        # de instacias, se le tiene que adicionar el parametro many= True para indicar que lo tendra que iterar
        niveles = dto.dump(resultado, many=True)
        
        niveles = []
        for nivel in resultado:
           niveles.append({
               'id' : nivel.id,
               'numero' : nivel.numero,
               'descripcion' : nivel.descripcion

           })
        return {
               'content' : niveles
        }
    
    def post(self):
        data = request.json 
        dto =NivelDto()
        #load > aca le pasamos un diccionario y lo convertira y validara  si toda la informacion es correcta, si no o es , emitira error y si la informacion esta bien un diccionario con la data correcta
        try:
            data_validada =dto.load(data)
            print(data_validada)

            nuevo_nivel = Nivel(numero=data.get('numero'), descripcion=data.get
            ('descripcion'))
            # con el metodo add indicam,os que queremos guardar registro
            conexion.session.add(nuevo_nivel)
            # con el metodo commit queremos guaradr de marea permanete esa informacion en la baase de datos
            conexion.session.commit()

            return {
                'message' : 'Nivel creado exitosamente'
            }, 201 
        except Exception as error:
            return {
            'message': 'Error al crear el nivel',
            'content': error.args
            }


              