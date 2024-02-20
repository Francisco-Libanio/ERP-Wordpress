# Formulários do  site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from ERP.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=(DataRequired()))
    botao_confirmacao = SubmitField("Fazer login")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = SubmitField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha",
                          validators=[DataRequired(), Length(6, 15, 'O número de caracteres deve estar entre 5 e 15')])
    confirmar_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado faça login para continuar")


class CadastrarProduto(FlaskForm):
    ...


class FaleConosco():
    ...
