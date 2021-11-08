from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField, SubmitField, FloatField

# Creating Login Form contains email and password
class BookForm(FlaskForm):
    title = StringField('title', validators=[validators.InputRequired(message='Title field must not be empty')])
    author = StringField('author', validators=[validators.InputRequired(message='Author field must not be empty')])
    date_published = StringField('date_published', validators=[validators.InputRequired(message='Date field must not be empty')])

class SearchForm(FlaskForm):
    search_title = StringField('search_title', validators=[])
    search_author = StringField('search_author', validators=[])
    date_start = StringField('date_start', validators=[])
    date_end = StringField('date_end', validators=[])
