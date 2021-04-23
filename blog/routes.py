from flask import render_template, url_for, request, redirect, flash, Markup
from blog import app, db
from blog.models import User, Option, Questionnaire
from blog.forms import RegistrationForm, LoginForm, QuestionnaireForm, OptionForm
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import func, or_, desc, and_

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(isLecturer=form.isLecturer.data,id=form.userID.data,firstname=form.firstname.data,lastname=form.lastname.data,email=form.email.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('Login successful!')
      return redirect(url_for('home'))
    elif user is not None:
      flash(Markup('Incorrect password, please try again!'))
      return render_template('login.html',title='Login',form=form, search_form=search_form)
    flash(Markup('There is no user account for this email address. Would you like to <a href="/register">Register?</a>'))
    return render_template('login.html',title='Login',form=form, search_form=search_form)
  return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
  logout_user()
  flash('Logout successful!')
  return redirect(url_for('home'))

@app.route("/grouplist",methods=['GET','POST'])
@login_required
def grouplist():
    students=User.query.filter(User.isLecturer==False)
    return render_template('grouplist.html',title='Grouplist',students=students)

@app.route("/groups",methods=['GET','POST'])
@login_required
def groups():
    students=User.query.filter(User.isLecturer==False)
    return render_template('groups.html',title='Groups',students=students)

@app.route("/questionnaire",methods=['GET','POST'])
@login_required
def questionnaire():
  form = QuestionnaireForm()
  if form.validate_on_submit():
      current_user.priorProgExp=form.priorProgExp.data
      current_user.priorSTEMDegree=form.priorSTEMDegree.data
      db.session.commit()
      return redirect(url_for('home'))
  return render_template('questionnaire.html',title='Questionnaire',form=form)

@app.route("/groupallocations",methods=['GET','POST'])
@login_required
def groupallocations():
    intialStudents=User.query.filter(User.isLecturer==False)
    Exp2STEM = []
    Exp1STEM = []
    Exp0STEM = []
    Exp2NoSTEM = []
    Exp1NoSTEM = []
    Exp0NoSTEM = []

    for student in intialStudents:
        if student.priorProgExp == 2 and student.priorSTEMDegree == True:
            Exp2STEM.append(student)
        elif student.priorProgExp == 1 and student.priorSTEMDegree == True:
            Exp1STEM.append(student)
        elif student.priorProgExp == 0 and student.priorSTEMDegree == True:
            Exp0STEM.append(student)
        elif student.priorProgExp == 2 and student.priorSTEMDegree == False:
            Exp2NoSTEM.append(student)
        elif student.priorProgExp == 1 and student.priorSTEMDegree == False:
            Exp1NoSTEM.append(student)
        elif student.priorProgExp == 0 and student.priorSTEMDegree == False:
            Exp0NoSTEM.append(student)

    numberOfGroups = 10

    listOfGroups = []
    for x in range(numberOfGroups):
        listOfGroups.append([x+1])


    def allocateCategoryOfStudents(category, startingGroupNumber):
        if len(category) == 0:
            return startingGroupNumber
        for x in range(startingGroupNumber, len(listOfGroups)):
            if len(category) > 0:
                listOfGroups[x].append(category.pop())
            else:
                return listOfGroups[x][0]-1
        while len(category) > 0:
            for group in listOfGroups:
                if len(category) > 0:
                    group.append(category.pop())
                else:
                    return group[0]-1

    x = allocateCategoryOfStudents(Exp2STEM, 0)
    y = allocateCategoryOfStudents(Exp1STEM, x)
    z = allocateCategoryOfStudents(Exp0STEM, y)
    a = allocateCategoryOfStudents(Exp2NoSTEM, z)
    b = allocateCategoryOfStudents(Exp1NoSTEM, a)
    c = allocateCategoryOfStudents(Exp0NoSTEM, b)

    for group in listOfGroups:
      for x in range(1,len(group)):
        group[x].group = group[0]

    db.session.commit()

    students=User.query.filter(User.isLecturer==False)

    return render_template('groupallocations.html',title='Groupallocations',students=students, numberOfGroups = numberOfGroups)

@app.route("/optionform",methods=['GET','POST'])
@login_required
def optionform():
  form = OptionForm()
  option1 = Option.query.filter(Option.optionID==1)
  option2 = Option.query.filter(Option.optionID==2)

  if form.validate_on_submit():
      option1.priority=form.option1.data
      option2.priority=form.option2.data
      db.session.commit()
      return redirect(url_for('home'))
  return render_template('optionform.html',title='OptionForm',form=form)
