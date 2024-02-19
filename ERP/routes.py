from flask import render_template, url_for
from ERP import app
from flask_login import login_required


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/login")
def login():
    render_template('login.html')


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('Perfil.html', usuario=usuario)


@app.route('/Cadastro-de-produtos')
@login_required
def cadastro():
    return render_template("Cadastro-de-produtos.html")


@app.route('/Estoque')
@login_required
def estoque():
    return render_template('Estoque.html')


@app.route('/selecao-de-modulo')
@login_required
def selecao():
    return render_template('selecao-de-modulo.html')
