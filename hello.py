from flask import Flask

app = Flask(__name__)

@app.route('/')
def indice():
    return "Hola, Mundo. Estoy funcionando."

@app.route("/adios")
def elnombredefuncionquequiera():
    return "Pues adios"