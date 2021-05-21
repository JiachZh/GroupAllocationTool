from flask import render_template, url_for, request, redirect, flash, Markup
from blog import app, db
from blog.models import User, Option, Questionnaire
from blog.forms import RegistrationForm, LoginForm, QuestionnaireForm, OptionForm # GroupAllocationForm
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

@app.route("/lecturerPage",methods=['GET','POST'])
@login_required
def lecturerPage():
  return render_template('lecturerPage.html')

@app.route("/questionnaire",methods=['GET','POST'])
@login_required
def questionnaire():
  form = QuestionnaireForm()
  if form.validate_on_submit():
      current_user.priorProgExp=form.priorProgExp.data
      current_user.priorSTEMDegree=form.priorSTEMDegree.data
      current_user.gender=form.gender.data
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

  totalFemale = User.query.filter(and_(User.isLecturer==False, User.gender=="F")).count()
  totalMale = User.query.filter(and_(User.isLecturer==False, User.gender=="M")).count()
  if totalMale >= totalFemale:
      majorityGender = "M"
  else:
      majorityGender = "F"

  print(majorityGender)
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
    if genderPairs == 1:
        if gender == majorityGender or gender == "O":
            studentScoresMajGender.append((student, score))
        else:
            studentScoresMinGender.append((student, score))
    else:
        allStudentScores.append((student, score))

  #NEED TO SORT LISTS BY SCORE BEFORE ALLOCATION
  studentScoresMajGender = sorted(studentScoresMajGender, key = lambda x:x[1], reverse=True)
  studentScoresMinGender = sorted(studentScoresMinGender, key = lambda x:x[1], reverse=True)
  allStudentScores = sorted(allStudentScores, key = lambda x:x[1], reverse=True)
  print("majority gender", studentScoresMajGender)
  print("minority gender", studentScoresMinGender)
  listOfGroups = []
  for x in range(numberOfGroups):
      listOfGroups.append([x+1])

  if genderPairs == None or genderPairs ==0:
      while len(allStudentScores) > 0:
          for group in listOfGroups:
              if len(allStudentScores) > 0:
                  group.append(allStudentScores.pop(0)) #does pop go from start? need to pop highest score

  else:
    while (len(studentScoresMinGender)>0) or (len(studentScoresMajGender)>0):
      for group in listOfGroups:
        if len(studentScoresMinGender)>0:
          if len(studentScoresMinGender)<=3:
            print("remainder of minorit gender being added", studentScoresMinGender)
            print("to group", group[0])
            group.extend(studentScoresMinGender)
            studentScoresMinGender.clear()
          else:
              print("student being added", studentScoresMinGender[0])
              print("to group", group[0])
              group.append(studentScoresMinGender.pop(0)) #add minorityGender with highest score
              print("student being added", studentScoresMinGender[-1])
              print("to group", group[0])
              group.append(studentScoresMinGender.pop(-1))
        else:
          #check if group is full
          if len(group)>numberOfStudentsPerGroup:
            continue
          else:
            if len(studentScoresMajGender)>1:
              print("student being added", studentScoresMajGender[0])
              print("to group", group[0])
              group.append(studentScoresMajGender.pop(0)) #add majGender with highest score     
              print("student being added", studentScoresMajGender[-1])
              print("to group", group[0])
              group.append(studentScoresMajGender.pop(-1))
            elif len(studentScoresMajGender)>0:
              print("student being added", studentScoresMajGender[0])
              print("to group", group[0])
              group.append(studentScoresMajGender.pop(0))
            else:
              break

    # while len(studentScoresMinGender) > 0:
    #     for group in listOfGroups:
    #         if len(studentScoresMinGender)<=3:
    #           group.extend(studentScoresMinGender)
    #           studentScoresMinGender.clear()
    #         else:
    #             group.append(studentScoresMinGender.pop(0)) #add minorityGender with highest score
    #             group.append(studentScoresMinGender.pop(-1)) #add minorityGender with lowest score
    #         group.append(studentScoresMajGender.pop(0)) #add majGender with highest score
    #         group.append(studentScoresMajGender.pop(-1))#add majGender with lowest score
    # while len(studentScoresMajGender) > 0:
    #     for group in listOfGroups:
    #         if len(studentScoresMajGender) > 0:
    #             group.append(studentScoresMajGender.pop(0))
    #         else:
    #             break

  for group in listOfGroups:

    for x in range(1,len(group)):
        group[x][0].group = group[0]

  db.session.commit()

  students=User.query.filter(User.isLecturer==False)
  return render_template('groups.html',title='Groups',students=students)


@app.route("/optionform",methods=['GET','POST'])
@login_required
def optionform():
  form = OptionForm()

  if form.validate_on_submit():
      Option.query.filter_by(optionID=1).update({'priority':form.option1.data})
      Option.query.filter_by(optionID=2).update({'priority':form.option2.data})
      Option.query.filter_by(optionID=3).update({'priority':form.option3.data})
      Option.query.filter_by(optionID=4).update({'priority':form.option4.data})
      db.session.commit()
      return redirect(url_for('lecturerPage'))
  return render_template('optionform.html',title='OptionForm',form=form)
