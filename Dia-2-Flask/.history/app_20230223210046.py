from flask import Flask

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