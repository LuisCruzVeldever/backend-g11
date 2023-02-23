def saludar(nombre):
    saludo =  'Hola {}'. format(nombre)
    print(saludo)

saludar('Luis')

def saludar_varios(*args):
    # cuando nosotros colocamps en un parametro el '*' significa que no
    # hay limite de ese parametro, este parametro debe ir al ultimo
    # todos los valores que le pasamos a este patrametro se almacenaran en una tupla
    # NOTA: las tuplas , a diferencia de los arreglos, no se pueden modificar osea una vez creadas sus valores no pueden cambiar
    print(args)
    for nombre in args:
        saludo = 'Hola {}'.format(nombre)
        print(saludo)

saludar_varios('Roaxana', 'Juana', 'Martin', 'Roberto')
saludar_varios('Pedro', 'Luis')
saludar_varios()
saludar_varios('Eduardo', 20, True, 10.5)

def informacion_usuario(**kwargs):
# kwargs > keyboard argument o se le pasan parametros por llaves 
    print(kwargs)
# .get('llaves') > devolver el valor si es que existe la llave, si no existe entonces devolvera None
    print(kwargs.get('estatura', 'NO HAYYYYYYY'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre = 'Luis', edad = 30, estado_civil='soltero' , estatura= 1.72)
informacion_usuario(nombre = 'Pamela', apellido='Juarez', nacionalidad= 'Colombiana', fecha_nacimiento = '04/06/1982')
print('ADIOSSSSSS')

# recibir dos valores y hacer la division (dividendo / divisor) y retornar su resultado
def dividir(dividendo, divisor):
    #si la division da un error retornar un mensaje que diga 'divison incorrecta'
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return 'No puede haber division entre 0'
    except TypeError:
        # ingresara si la division tiene algun caracter
        return 'Las divisiones solamnente pueden ser enttre dos numeros'
    
    except:
        # ingresara si no es ninguno de los errores anteriores
        return 'Error desconocido'

valor = dividir(10,5)
print(valor)

valor = dividir(10,0)
print(valor)

valor = dividir ('a', 'h')
print(valor)

try:
    valor = (5,)
    print(valor)
except TypeError:
    print('Estuvo mal llamar asi a la función')