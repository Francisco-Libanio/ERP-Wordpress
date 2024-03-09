from flask import render_template, url_for, redirect
from ERP import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from ERP.forms import FormLogin, FormCriarConta, FormFoto, FormProduto
from ERP.models import Usuario, Foto, Produto
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario:
            bcrypt.check_password_hash(usuario.senha, formlogin.senha.data)
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
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
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=formcriarconta)


@app.route('/perfil/<id_usuario>', methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        form_produto = FormProduto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)

            #salvar o arquivo na pasta foto_post
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)

            #registrar esse arquivo no banco de dados
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()

        if form_produto.validate_on_submit():
            produto = Produto(
                nome=form_produto.nome.data,
                preco=form_produto.preco.data,
                quantidade=form_produto.quantidade.data,
                marca=form_produto.marca.data,
                modelo=form_produto.modelo.data,
                codigoDeBarras=form_produto.codigoDeBarras.data,
                plataformaDeVenda=form_produto.plataformaDeVenda.data,
                largura=form_produto.largura.data,
                altura=form_produto.altura.data,
                profundidade=form_produto.profundidade.data,
                pesoBruto=form_produto.pesoBruto.data,
                pesoLiquido=form_produto.pesoLiquido.data,
                cadastradoPor=form_produto.cadastradoPor.data
            )
            # Adicione o produto ao banco de dados
            database.session.add(produto)
            database.session.commit()

        return render_template('Perfil.html', usuario=current_user, form=form_foto, formp=form_produto)

    else:  # esse else permite o usuario ver o perfil de outros usuarios
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('Perfil.html', usuario=usuario, form=None, formp=None)


@app.route('/Cadastro-de-produtos', methods=["GET", "POST"])
@login_required
def cadastro():
    form_produto = FormProduto()

    if form_produto.validate_on_submit():
        produto = Produto(
            nome=form_produto.nome.data,
            preco=form_produto.preco.data,
            quantidade=form_produto.quantidade.data,
            marca=form_produto.marca.data,
            modelo=form_produto.modelo.data,
            codigoDeBarras=form_produto.codigoDeBarras.data,
            plataformaDeVenda=form_produto.plataformaDeVenda.data,
            largura=form_produto.largura.data,
            altura=form_produto.altura.data,
            profundidade=form_produto.profundidade.data,
            pesoBruto=form_produto.pesoBruto.data,
            pesoLiquido=form_produto.pesoLiquido.data,
            cadastradoPor=form_produto.cadastradoPor.data
        )
        # Adicione o produto ao banco de dados
        database.session.add(produto)
        database.session.commit()
        # Redirecione para evitar que o formulário seja enviado novamente ao atualizar a página
        return redirect(url_for('cadastro'))

    return render_template('Cadastro-de-produtos.html', formp=form_produto)



@app.route('/Estoque')
@login_required
def Estoque():
    produtos = Produto.query.order_by(Produto.dataDeCadastro.desc()).all() #para limitar basta colocar [:100]
    return render_template('Estoque.html', produtos=produtos)


@app.route('/selecao-de-modulo')
@login_required
def selecao():
    return render_template('selecao-de-modulo.html')


@app.route("/logout")

def logout():
    logout_user()
    return redirect(url_for("homepage"))
