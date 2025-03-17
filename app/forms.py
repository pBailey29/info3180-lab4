from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('Upload Image', validators=[
        FileRequired(message='Please select a file'),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Only images allowed! (jpg, png, jpeg)')
    ])
    submit = SubmitField('Upload')