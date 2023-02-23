class Persona:
    # cuando una variable se define dentro de una clase pasa a llamarse ATRIBUTO
    estatura = 1.80
    peso = 80
    signo_zodiacal = 'LEO'
    
    def sumar(self, *args):
# self = para hacer referencia a la misma clase, es como el this caso de js, c#
# cuando una funcion se declara o se define dentro de una clase pasa a llamarse METODO
#Recibir un numero ilimitado d enumeros para realizar  su sumatoria
        total = 0
    # args = (10,5,41,526,489,63)
        for numero in args:
            total = total + numero
        return total
    
    def saludar(self, nombre):
        return 'Hola {}' .format(nombre)
    
# cuando sacamos una 'copia' de la clase para utilizarla estamos creando una instancia
persona1 = Persona ()
persona2 = Persona ()

# modifico los atributos de esa persona en particular
persona1.peso = 70
persona2.peso = 50

# todas las modificaciones que hacemos es independiente de la instancia

print(persona1.peso)
print(persona2.peso)

resultado1 = persona1.sumar(10,5,41,526,489,63)
resultado2 = persona2.sumar(5,8,65,985,492,520,700)

print(resultado1)
print(resultado2)

