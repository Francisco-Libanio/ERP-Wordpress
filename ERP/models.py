# Criar a estrutura do banco dedados
from ERP import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class Produto(database.Model):
    codigo_id = database.Column(database.Integer, primary_key=True)
    dataDeCadastro = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    nome = database.Column(database.String, nullable=False)
    preco = database.Column(database.Float)
    quantidade = database.Column(database.Integer)
    marca = database.Column(database.String)
    modelo = database.Column(database.String)
    codigoDeBarras = database.Column(database.String, nullable=False, unique=True)
    plataformaDeVenda = database.Column(database.String)
    largura = database.Column(database.Float)
    altura = database.Column(database.Float)
    profundidade = database.Column(database.Float)
    pesoBruto = database.Column(database.Float)
    pesoLiquido = database.Column(database.Float)
    cadastradoPor = database.Column(database.String)
