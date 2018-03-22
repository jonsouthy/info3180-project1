from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import StringField, SelectField


class signForm(FlaskForm):
    fname = StringField('First Name',validators=[FileRequired()])
    lname = StringField('Last Name',validators=[FileRequired()])
    gender = SelectField (label='Gender', choices=[("Male","Male"),("Female","Female")])
    email = StringField('Email Address',validators=[FileRequired()])
    location = StringField('Location',validators=[FileRequired()])
    biography = StringField('Biography',validators=[FileRequired()])
    upload = FileField('Upload Profile Image', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'],'Only image files are accepted, i.e. jpg, jpeg & png')])
    