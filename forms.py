from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class Contact(FlaskForm):
    
    username = StringField(
        "Name",
        validators=[DataRequired(), Length(4,15)]
    )

    phonenumber = StringField(
        "Phone Number",
        validators=[DataRequired(), Length(10,10)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField("Submit")