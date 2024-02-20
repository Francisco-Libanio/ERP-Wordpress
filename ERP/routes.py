from flask import render_template, url_for
from ERP import app, database, bcrypt
from flask_login import login_required
from ERP.forms import FormLogin, FormCriarConta
from ERP.models import Usuario, Foto


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template('login.html', form=formlogin)


@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data,
                          senha=senha, email=formcriarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
    return render_template("criarconta.html", form=formcriarconta)


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('Perfil.html', usuario=usuario)


@app.route('/Cadastro-de-produtos')
def cadastro():
    return render_template("Cadastro-de-produtos.html")


@app.route('/Estoque')
def estoque():
    return render_template('Estoque.html')


@app.route('/selecao-de-modulo')
def selecao():
    return render_template('selecao-de-modulo.html')
