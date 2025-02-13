from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FormField, TextAreaField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, EqualTo, InputRequired, Length
from flask_wtf.file import FileAllowed
from app import photos

# defines all forms in the application, these will be instantiated by the template,
# and the routes.py will read the values of the fields

class LoginForm(FlaskForm):
    username = StringField('Username', render_kw={'placeholder': 'Username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder': 'Password'}, validators=[DataRequired()])
    remember_me = BooleanField('Remember me') # TODO: It would be nice to have this feature implemented, probably by using cookies
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', render_kw={'placeholder': 'First Name'}, validators=[DataRequired()])
    last_name = StringField('Last Name', render_kw={'placeholder': 'Last Name'}, validators=[DataRequired()])
    username = StringField('Username', render_kw={'placeholder': 'Username'}, validators=[DataRequired()])
    password = PasswordField('Password', render_kw={'placeholder': 'Password'}, validators=[InputRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', render_kw={'placeholder': 'Confirm Password'}, validators=[EqualTo('password', message='Passwords must match!')])
    submit = SubmitField('Sign Up')

class IndexForm(FlaskForm):
    login = FormField(LoginForm)
    register = FormField(RegisterForm)

class PostForm(FlaskForm):
    content = TextAreaField('New Post', render_kw={'placeholder': 'What are you thinking about?'})
    image = FileField('Image', validators=[FileAllowed(photos, 'Images only!')])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('New Comment', render_kw={'placeholder': 'What do you have to say?'})
    submit = SubmitField('Comment')

class FriendsForm(FlaskForm):
    username = StringField('Friend\'s username', render_kw={'placeholder': 'Username'})
    submit = SubmitField('Add Friend')

class ProfileForm(FlaskForm):
    education = StringField('Education', render_kw={'placeholder': 'Highest education'})
    employment = StringField('Employment', render_kw={'placeholder': 'Current employment'})
    music = StringField('Favorite song', render_kw={'placeholder': 'Favorite song'})
    movie = StringField('Favorite movie', render_kw={'placeholder': 'Favorite movie'})
    nationality = StringField('Nationality', render_kw={'placeholder': 'Your nationality'})
    birthday = DateField('Birthday')
    submit = SubmitField('Update Profile')
