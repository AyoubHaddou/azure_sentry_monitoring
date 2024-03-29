from flask_wtf import FlaskForm

from wtforms import PasswordField, EmailField, SubmitField, StringField, TextAreaField, FileField, BooleanField
from wtforms.fields import DateField, SelectField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

class Login(FlaskForm):
    """[Form to login]
    """
    email = EmailField(label="Adresse mail:", validators=[DataRequired()])
    password = PasswordField(label="Mot de passe:",
                             validators=[DataRequired()])
    submit = SubmitField(label="Login")

class AddUser(FlaskForm):
    """[Form to add user]
    """
    last_name = StringField(label='Nom', validators=[DataRequired()])
    first_name = StringField(label='Prénom', validators=[DataRequired()])
    email_address = StringField(label='Email', validators=[DataRequired()])
    password_hash = PasswordField(label='Mot de passe', validators=[DataRequired()])
    password_hash2 = PasswordField(label='Confirmez votre mot de passe', validators=[DataRequired()])
    submit = SubmitField(label='Ajouter')