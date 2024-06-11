from flask import Flask, jsonify,request, render_template, redirect, url_for, flash 
from Models import db, Admin
import sqlite3

app = Flask(__name__, static_url_path="/static")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/palac/Documents/prueba-web/escuela.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'tu_clave_secreta_aqui'
db.init_app(app)



# rutas
@app.route('/')
def home():
    titulo = "Escuela Metropolitana"

    return render_template('index.html', titulo=titulo)

# ruta para nosotros
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if not usuario or not password:
            flash('Todos los campos son requeridos', 'error')

        admin = Admin.query.filter_by(usuario=usuario, password=password).first()

        if admin:
            flash('Inicio exitoso', 'success')
            return redirect(url_for('profesor'))
        else:
            flash('Correo electrónico o contraseña incorrectos', 'error')  
            return redirect(url_for('login'))  

        
    else:
        titulo = "Inicio de sesión"
        return render_template('login.html', titulo=titulo)

# instrucciones
@app.route('/instrucciones')
def instrucciones():
    titulo = "Instrucciones"
    return render_template('instrucciones.html', titulo=titulo)

# profesor
@app.route('/profesor')
def profesor():
    titulo = "Profesor"

    return render_template('profesor.htm', titulo=titulo)

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True, port=4000)