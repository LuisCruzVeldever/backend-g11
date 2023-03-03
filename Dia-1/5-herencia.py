class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print('Buenos dias!')

class Beneficio:
    def saludar(self, detalle):
        self.detalle = detalle
    
    def mostrar_beneficios(self):
        return{
            'detalle': self.detalle
        }

class Alumno(Persona):
    def __init__(self, nombre, apellido, grado):
        self.grado = grado
        # llamando al constructor de la clase que estoy hererdando
        super().__init__(nombre, apellido)

    def saludar(self):
        #Polimorfismo > poli (muchas) morfa (formas) > dependiendo de donde se made a llamara al metodo este tendra un comportamiento u otro, 
        #en este caso estamos modificando el comportamiento del metaod de la clase padre "saludar"
        saludo_padre = super().saludar()
        print(saludo_padre + 'Yos soy un alumno')

    def dar_vueltas(self):
        print ('Dando vuletas. . .')
        
class Docente(Persona, Beneficio):
    def __init__(self, nombre, apellido, seguro_social, detalle):
        self.seguro_social= seguro_social
        #pi
        Persona.__init__(self, nombre, apellido)
        Beneficio.__init__(self, detalle)


    def evaluar(self):
        print ('Evaluando. . .')

    
luis = Alumno('luis', 'cruz', 'veldever')
paolo = Docente('paolo','soncco', '41538233')

luis.saludar()
print(paolo.saludar())

print(luis.nombre)