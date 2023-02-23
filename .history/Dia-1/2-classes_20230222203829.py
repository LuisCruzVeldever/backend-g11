class Persona:
    estatura = 1.80
    peso = 80
    signo_zodiacal = 'LEO'

# self = para hacer referencia a la misma clase, es como el this caso de js, c#
    def sumar(self, numero1, numero2):
        return numero1 + numero2
    
    def saludar(self, nombre):
        return 'Hola {}' .format(nombre)
    
# cuando sacamos una 'copia' de la clase para utilizarla estamos creando una instancia

persona1 = Persona ()
persona2 = Persona ()

# modifico los atributos de esa persona en particular
persona1.peso = 70
persona2.peso = 50

print(persona1.peso)
print(persona2.peso)