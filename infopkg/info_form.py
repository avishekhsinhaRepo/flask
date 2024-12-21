from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class InfoForm(FlaskForm):
    breed = StringField("What Breed are you?")
    submit = SubmitField("Submit")