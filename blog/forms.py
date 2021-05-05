from flask import flash
from flask_wtf import FlaskForm
from blog.models import User, Option, Questionnaire
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Length, Email, ValidationError, Regexp, EqualTo


class RegistrationForm(FlaskForm):
    isLecturer = BooleanField('Are you a Lecturer?')
    userID = IntegerField('Staff or Student ID', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=3, max=15, message='First name must be between 3 and 15 characters long.')])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=3, max=15, message='Last name must be between 3 and 15 characters long.')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Regexp('^(?=.*\d).{8,15}$', message='Your password should be between 8 and 15 characters long, and contains at least one numeric digit.'),
        EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(userName=username.data).first()
        if user:
            raise ValidationError('Username already exist. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address is already associated with an account.')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            flash('User not exist or password wrong.')
    
class QuestionnaireForm(FlaskForm):
    priorProgExp = RadioField('Select your level of programming experience', validators=[InputRequired()],choices=[('0', 'None'),('1','Some'),('2', 'Lots')])
    priorSTEMDegree = BooleanField('Do you hold a STEM degree (....)',validators=[InputRequired()])
    gender = RadioField('Gender', validators=[InputRequired()], choices= [('M', 'Male'), ('F', 'Female'), ('O', 'Prefer not to say')])
    submit = SubmitField('Submit')

class OptionForm(FlaskForm):
    option1 = RadioField("1. Students' level of programming experience", choices=[('1', '1'),('2','2'),('3', '3')])
    option2 = RadioField('2. Whether students hold a STEM Degree', choices=[('1', '1'),('2','2'),('3', '3')])
    option3 = BooleanField('3. Would you rather avoid having students being the only male or female in their team? Select if yes.')
    option4 = RadioField('Select the number of students in each group', validators = [InputRequired()], choices=[('5', '5'), ('6', '6')])
    submit = SubmitField('Submit')
