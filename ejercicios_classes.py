from pprint import pprint

class OperacionesMatematicas:

    def __init__(self, valor_1, valor_2): # dentro de metodo magico nuestros (self, valor_1, valor_2) el self no cuenta , valores definimos recibimos 2 valores valor_1 valor_2 
        self.a = valor_1
        self.b = valor_2


    def sumar (self):      #creamos nuestro metodo 
        return self.a + self.b    #retornamos la suma o la condicion 
    
    def restar (self):
        return self.a - self.b 
    
    def multiplicar (self):
        return self.a * self.b 
    
    def dividir (self):
        return self.__redondear(self.a / self.b)

    def __redondear(self, numero):
        return round(numero, 2)   #redondear el primero es el numero , el 2 son los decimales

operaciones = OperacionesMatematicas(5, 3)  #estamos llamando a nuestra variable 

# print (operaciones.dividir())

# ejercicio 2:   crear una clase usuario que reciba los datos de un usuario 
# (nombre, edad, dni, estatura, estado civil) y convertir estos datos en un diccionario 
   

class Usuario:
    def __init__(self, nombre, edad, dni, estatura, estadoCivil):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estadoCivil = estadoCivil

    def convertirDiccionario(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'dni': self.dni,
            'estatura': self.estatura,
            'estadoCivil': self.estadoCivil
        }
    
usuario = Usuario('Luis', 40, 41538233, 1.72, 'soltero')

pprint (usuario.convertirDiccionario())


