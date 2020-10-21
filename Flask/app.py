from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta'


@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario ya ha hecho login {session["username"]}'
    return 'No ha hecho login'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # omitimos validacion de usuario y password
        usuario = request.form['username']
        # agregar usuario a la session
        session['username'] = usuario
        # session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))




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


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pag_no_encontrada(error):
    return render_template('error404.html', error=error), 404


# Representational state transfer
@app.route('/api/mostrar/<nombre>/', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)
