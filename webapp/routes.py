from webapp import app

@app.route("/")
def indice():
    return "Flask funciona"

@app.route("/adios")
def adios():
    return "Pues adios"

@app.route("/peliculas")
def pelis():
    return "Aqui irán las pelis"
