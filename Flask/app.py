from flask import Flask, request, render_template, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return 'Hola Mundo desde Flask'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'tu edad es: {edad}'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    # return f'tu nombre es {nombre}'
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    # return redirect(url_for('inicio'))
    return redirect(url_for('mostrar_nombre', nombre='Juan'))
