# Formulários do  site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from ERP.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[(DataRequired())])
    botao_confirmacao = SubmitField("Fazer login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha",
                          validators=[DataRequired(), Length(6, 15, 'O número de caracteres deve estar entre 5 e 15')])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado faça login para continuar")


class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")


class FormProduto(FlaskForm):
    nome = StringField("Nome do produto", validators=[DataRequired()])
    preco = IntegerField("Preço de venda", validators=[DataRequired()])
    quantidade = IntegerField("Quantida em estoque", validators=[DataRequired()])
    marca = StringField("Marca")
    modelo = StringField("Modelo")
    codigoDeBarras = StringField("Código de barras")
    plataformaDeVenda = StringField("Site ou loja")
    largura = FloatField("Largura do produto (cm)")
    altura = FloatField("Altura produto (cm)")
    profundidade = FloatField("Profundidade do produto (cm)")
    pesoBruto = FloatField("Peso do produto Bruto (g)")
    pesoLiquido = FloatField("PEso do produto Liquido (g)")
    cadastradoPor = StringField("Cadastrado por")
    botao_confirmacao = SubmitField("Enviar")
