from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenidos a mi primera API con Flask 😁"

@app.route("/alumno")
def alumno():
   return {
       'nombre': 'Luis',
       'edad' : 37,
       'promedio': 18
    }

lista_alumnos = [
        {
       'nombre': 'Jose',
       'edad' : 36,
       'promedio': 17
    },
    {
       'nombre': 'Andres',
       'edad' : 30,
       'promedio': 19
    }
]
@app.route("/alumnos", methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def alumnos():
  if request.method == 'GET':
    return lista_alumnos
  elif request.method == 'POST':
    # metodos para obtener el body (request.jason) ó (request.get_json())
    lista_alumnos.append(request.json)
    return lista_alumnos

@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno['nombre'] == nombre:
            return alumno
    return {
        'message': 'El alumno no existe'
    }

# debug= True  => SI REALIZAMOS ALGUNCAMBIO PODREMOS VERLO EN TIEMPO REAL (SE REINICIARÁ EL SERVIDOR)
app.run(debug=True)