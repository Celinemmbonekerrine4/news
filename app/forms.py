from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class articleForm(FlaskForm):

    name = StringField('Article name', validators=[Required()])
    article = TextAreaField('News article', validators=[Required()])
    submit = SubmitField('Submit')
