from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField


class uploadForm(FlaskForm):
    upload = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'],'Only image files are accepted, i.e. jpg, jpeg & png')])