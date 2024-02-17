from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/login")
def login():
    render_template('login.html')


@app.route('/perfil/<usuario>')
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


if __name__ == "__main__":
    app.run(debug=True)
