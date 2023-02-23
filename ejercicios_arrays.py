from pprint import pprint
# Ordenar habitantes
ciudades = [
    {
        'nombre': 'Tumbes',
        'habitantes': 500000    
    },
    {
        'nombre': 'Arequipa',
        'habitantes': 800000
    },
    {
        'nombre': 'Loreto',
        'habitantes': 10000 
    }
]

def habitante(ciudad):
    return ciudad['habitantes']

ciudades.sort(key=habitante, reverse=True) # primero lo ordena
ciudades.append ({'nombre': 'Cusco', 'habitantes': 20000})
# ciudades.pop(0)
# ciudades.pop(0)
# ciudades.remove({'nombre': 'Cusco', 'habitantes': 20000})

index = 0
for ciudad in ciudades:
    if ciudad['nombre'] == 'Cusco':
        ciudades.remove(ciudades[index])
    index = index + 1
    # index += 1 es igual al index = index +1 
# pprint(ciudades)
    
lista = ['Arequipa', 'Cusco', 'Tumbes']
# lista.remove('Arequipa')
# print(lista)

for x, y in enumerate(lista):
    print(x, y)