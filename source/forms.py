from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, \
    EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username, userCollection):
        query = {"username": username.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That username is taken. \
                Please choose a different one.')

    def validate_email(self, email, userCollection):
        query = {"email": email.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That email is taken. \
                Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = Tempuser.objects(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. \
                    Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Tempuser.objects(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. \
                    Please choose a different one.')


class HousingForm(FlaskForm):
    name = StringField('Housing Name', validators=[DataRequired()])
    address = StringField('Housing Address', validators=[DataRequired()])
    submit = SubmitField('Post')

# forms in endpoints


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        query = {"username": username.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That username is taken. \
                Please choose a different one.')

    def validate_email(self, email):
        query = {"email": email.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That email is taken. \
                Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. \
                    Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.objects(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. \
                    Please choose a different one.')


class HousingForm(FlaskForm):
    name = StringField('Housing Name', validators=[DataRequired()])
    address = StringField('Housing Address', validators=[DataRequired()])
    submit = SubmitField('Post')