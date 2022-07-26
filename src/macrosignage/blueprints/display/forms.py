from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class DisplayForm(FlaskForm):
    """
    Form for creating a new display.
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description',
                                validators=[Length(min=0, max=255)])
    submit = SubmitField('Create')
