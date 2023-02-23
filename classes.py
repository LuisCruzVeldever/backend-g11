class Vehiculo:
    def __init__(self, color, placa, marca):
        self.color = color
        self.placa = placa
        self.marca = marca

    def verificarEstado(self, fabricacion):
        return f'El vehiculo de color {self.color} fabricado en el año: {fabricacion}'
    
    def concatenarCaracteristicas(self):
        return f'El vehiculo con placa {self.placa}, de color {self.color} es de marca: {self.marca}'
    
   # def estado(self):
   #     return self.verificarEstado(2020)
        

vehiculo = Vehiculo("blanco", "bph-329", "Mazda")

# print(vehiculo.verificarEstado(1999))
# print(vehiculo.concatenarCaracteristicas())

class Alumno:
    def __init__(self, nom, ed):
        self.nombre = nom
        self.edad = ed

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
    def mostrarNombre(self):
        return self.nombre
    
    def mostrarEdad(self):
        return self.edad

    
x = Alumno('Luis', 40)

print (x)
# print (x.mostrarNombre())