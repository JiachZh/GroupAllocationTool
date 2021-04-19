from blog.models import Student, Module, Lecturer, Option, Questionnaire
from flask import render_template, url_for, request, redirect, flash, Markup
from blog import app, db
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import func, or_, desc, and_