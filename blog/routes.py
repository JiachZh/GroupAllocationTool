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
      return render_template('login.html',title='Login',form=form)
    flash(Markup('There is no user account for this email address. Would you like to <a href="/register">Register?</a>'))
    return render_template('login.html',title='Login',form=form)
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
    initialStudents=User.query.filter(User.isLecturer==False)
    STEM = Option.query.filter(Option.optionID==2).first()
    STEMpriority = STEM.priority
    PriorExp = Option.query.filter(Option.optionID==1).first()
    PriorExpPriority = PriorExp.priority
    gender = Option.query.filter(Option.optionID==3).first()
    genderPairs = gender.priority
    numberPerGroup = Option.query.filter(Option.optionID==4).first()
    numberOfStudentsPerGroup = numberPerGroup.priority
    totalNumberOfStudents = User.query.filter(User.isLecturer==False).count()
    numberOfGroups = round(totalNumberOfStudents/numberOfStudentsPerGroup)
    print("totalStudents=", totalNumberOfStudents)
    print("numPerGroup", numberOfStudentsPerGroup)
    print("numGroups", numberOfGroups)
    totalFemale = User.query.filter(and_(User.isLecturer==False, User.gender=="F")).count()
    totalMale = User.query.filter(and_(User.isLecturer==False, User.gender=="M")).count()
    if totalMale >= totalFemale:
        majorityGender = "M"
    else:
        majorityGender = "F"

    studentScoresMajGender = []
    studentScoresMinGender = []
    allStudentScores = []
    for student in initialStudents:
      if student.gender != None:
        gender = student.gender
      else:
        student.gender = "O"
      if student.priorSTEMDegree != None:
        STEM = student.priorSTEMDegree
        if STEM == True:
            STEMscore = STEMpriority
        else:
            STEMscore = 0
      else:
            STEMscore = 0
      if student.priorProgExp != None:
        PriorExp = student.priorProgExp
      else:
        PriorExp = 0
      PriorExpScore = PriorExp * PriorExpPriority
      score = STEMscore + PriorExpScore
      if genderPairs != None:
          if gender == majorityGender or gender == "O":
              studentScoresMajGender.append((student, score))
          else:
              studentScoresMinGender.append((student, score))
      else:
          allStudentScores.append((student, score))
    print("studentScoresMajGender",studentScoresMajGender)
    print("studentScoresMinGender", studentScoresMinGender)
    print("allStudentScores", allStudentScores)
    #NEED TO SORT LISTS BY SCORE BEFORE ALLOCATION
    studentScoresMajGender = sorted(studentScoresMajGender, key = lambda x:x[1], reverse=True)
    studentScoresMinGender = sorted(studentScoresMinGender, key = lambda x:x[1], reverse=True)
    allStudentScores = sorted(allStudentScores, key = lambda x:x[1], reverse=True)

    print("studentScoresMajGender",studentScoresMajGender)
    print("studentScoresMinGender", studentScoresMinGender)
    print("allStudentScores", allStudentScores)
    print("numGroups", numberOfGroups)
    listOfGroups = []
    for x in range(numberOfGroups):
        listOfGroups.append([x+1])
    print("groups:", listOfGroups)
    print("genderPairs", genderPairs)
    if genderPairs == None:
        while len(allStudentScores) > 0:
            for group in listOfGroups:
                if len(allStudentScores) > 0:
                    group.append(allStudentScores.pop(0)) #does pop go from start? need to pop highest score

    else:
      while len(studentScoresMinGender) > 0:
          for group in listOfGroups:
              if len(studentScoresMinGender) > 1:
                  group.append(studentScoresMinGender.pop(0)) #add minorityGender with highest score
                  group.append(studentScoresMinGender.pop(-1)) #add minorityGender with lowest score
              elif len(studentScoresMinGender) == 1:
                  group.append(studentScoresMinGender.pop())
              else:
                  group.append(studentScoresMajGender.pop(0)) #add majGender with highest score
                  group.append(studentScoresMajGender.pop(-1))#add majGender with lowest score
      while len(studentScoresMajGender) > 0:
          for group in listOfGroups:
              if len(studentScoresMajGender) > 0:
                  group.append(studentScoresMajGender.pop(0))
              else:
                  break

    for group in listOfGroups:
      print("group[0]", group[0])
      print("group: ", group)
      for x in range(1,len(group)):
          print(group[x][0].firstname)
          group[x][0].group = group[0]

    db.session.commit()

    students=User.query.filter(User.isLecturer==False)
    print("numGroups", numberOfGroups)
    return render_template('groupallocations.html',title='Groupallocations',students=students, numberOfGroups = numberOfGroups)


@app.route("/optionform",methods=['GET','POST'])
@login_required
def optionform():
  form = OptionForm()
  option1 = Option.query.filter(Option.optionID==1)
  option2 = Option.query.filter(Option.optionID==2)
  option3 = Option.query.filter(Option.optionID==3)


  if form.validate_on_submit():
      option1.priority=form.option1.data
      option2.priority=form.option2.data
      option3.priority=form.option3.data
      db.session.commit()
      return redirect(url_for('home'))
  return render_template('optionform.html',title='OptionForm',form=form)
