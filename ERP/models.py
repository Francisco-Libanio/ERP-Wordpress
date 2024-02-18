# Criar a estrutura do banco dedados
from ERP import database
from datetime import datetime


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, database.ForeignKey('produto.nome'), nullable=False)
    senha = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    foto = database.Column(database.String, default="default.png")
    dataDeCadastro = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())


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
    cadastradoPor = database.relationship("Usuario", backref="username", lazy=True)
