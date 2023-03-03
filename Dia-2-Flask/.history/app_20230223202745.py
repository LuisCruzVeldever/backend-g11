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


#debug => SI REALIZAMOS ALGUNCAMBIO PODREMOS VERLO EN TIEMPO REAL (SE REINICIARÁ EL SERVIDOR)

app.run(debug=True)