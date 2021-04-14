from datetime import datetime
from blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Student(UserMixin,db.Model):
  studentID=db.Column(db.Integer,primary_key=True)
  firstname=db.Column(db.String(15),nullable=False)
  lastname=db.Column(db.String(15),nullable=False)
  email=db.Column(db.String(120),unique=True,nullable=False)
  password_hash=db.Column(db.String(128))
  password=db.Column(db.String(60),nullable=False)
  priorProgExp=db.Column(db.Integer,primary_key=True)
  priorSTEMDegree=db.Column(db.Boolean,nullable=False,default=False)
  groupPerModule==db.Column(db.String(60),nullable=False)
  modules = db.relationship('Module', secondary=studentModules, backref=db.backref('students', lazy='dynamic'))

  def __repr__(self):
    return f"Student('{self.studentID}','{self.email}')"

class Module(db.Model):
  code = db.Column(db.String(15), primary_key=True)
  title = db.Column(db.Text, nullable=False)
  lecturer_id = db.Column(db.Integer, db.ForeignKey('lecturer.id'), nullable=False)

  def __repr__(self):
    return f"Module('{self.code}', '{self.title}')"

studentModules = db.Table('studentModules',
    db.Column('studentID', db.Integer, db.ForeignKey('student.studentID')),
    db.Column('moduleCode', db.String, db.ForeignKey('module.code'))
)

class Lecturer(db.Model):
  lecturerID=db.Column(db.Integer,primary_key=True)
  firstName=db.Column(db.String(15),nullable=False)
  lastName=db.Column(db.String(15),nullable=False)
  email=db.Column(db.String(120),unique=True,nullable=False)
  passwordHash=db.Column(db.String(128))
  password=db.Column(db.String(60),nullable=False)
  moduleCode=db.Column(db.String(50),nullable=False),
  is_admin=db.Column(db.Boolean,nullable=False,default=False)

  def __repr__(self):
    return f"Lecturer('{self.lecturerID}','{self.email}')"

  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')

  @password.setter
  def password(self,password):
    self.password_hash=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class Option(db.Model):
  optionID=db.Column(db.String(20),primary_key=True)
  priority=db.Column(db.Integer)
  studentAttribute=db.Column(db.String(20),nullable=False)
  questionWording=db.Column(db.Text,nullable=False)

  def __repr__(self):
    return f"Option('{self.optionID}','{self.studentAttribute}')"

class Questionnaire(db.Model):
  questionnaireID=db.Column(db.String(20),primary_key=True)
  option1=db.Column(db.String(20),nullable=False)
  option2=db.Column(db.String(20),nullable=False)
  option3=db.Column(db.String(20),nullable=False)

 def __repr__(self):
   return f"Questionnaire('{self.questionnaireID}')"
