from flask import Flask, jsonify,request, render_template 
#from Models import db, Streamers
#from logging import exception

app = Flask(__name__, static_url_path="/static")
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\escuela.db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db.init_app(app)



# rutas
@app.route('/')
def home():
    titulo = "Escuela Metropolitana"

    return render_template('index.html', titulo=titulo)

# ruta para nosotros
@app.route('/login')
def login():
    titulo = "Inicio de sesión"
    return render_template('login.html', titulo=titulo)

# instrucciones
@app.route('/instrucciones')
def instrucciones():
    titulo = "Instrucciones"
    return render_template('instrucciones.html', titulo=titulo)

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)