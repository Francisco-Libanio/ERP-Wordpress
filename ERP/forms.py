# Formulários do  site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from ERP.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[(DataRequired())])
    botao_confirmacao = SubmitField("Fazer login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            return ValidationError("Usuário inexistente, crie uma conta")


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
            return ValidationError("E-mail já cadastrado faça login para continuar")
