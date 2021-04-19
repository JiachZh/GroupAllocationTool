from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '9813c6984fe6e497bf8ee06cf7a1f414ceb884c665970f8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c2098620:8023Cake8023@csmysql.cs.cf.ac.uk:3306/c2098620_TeamQAllocationTool'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = 'Please log in to access this feature!'


from blog import routes

from blog.models import User, Option, Questionnaire
