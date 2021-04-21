from flask import render_template, url_for, request, redirect, flash, Markup
from blog import app, db
from blog.models import User, Option, Questionnaire
from blog.forms import RegistrationForm, LoginForm, QuestionnaireForm
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


# @app.route("/post/<int:post_id>")
# def post(post_id):
#   search_form=SearchForm()
#   post = Post.query.get_or_404(post_id)
#   comments = Comment.query.filter(Comment.post_id==post.id)

# #  Code for query using average adapted from https://stackoverflow.com/questions/7143235/how-to-use-avg-and-sum-in-sqlalchemy-query
# # accessed 08.2.2020, adapted to my particular search parameters and database details
# # end of referenced code.

#   ratings = db.session.query(func.avg(Rating.choice)).filter(Rating.post_id==post.id)
#   form = CommentForm()
#   rating_form = RatingForm()
#   tags = Tag.query.filter(Tag.post_id==post.id)
#   tag_form = TagForm()
#   remove_tag_form = RemoveTagForm()

#   return render_template('post.html',post=post,comments=comments, ratings=ratings, form=form, tags=tags, rating_form=rating_form, tag_form=tag_form, remove_tag_form=remove_tag_form,search_form=search_form)

# @app.route('/post/<int:post_id>/comment',methods=['GET','POST'])
# @login_required
# def post_comment(post_id):
#   search_form=SearchForm()
#   post=Post.query.get_or_404(post_id)
#   form=CommentForm()
#   if form.validate_on_submit():
#     db.session.add(Comment(content=form.comment.data,post_id=post.id,author_id=current_user.id))
#     db.session.commit()
#     flash("Your comment has been added to the post","success")
#     return redirect(f'/post/{post.id}')
#   comments=Comment.query.filter(Comment.post_id==post.id)
#   return render_templatee('post.html',post=post,comments=comments, form=form,search_form=search_form)



# @app.route('/post/<int:post_id>/rating',methods=['GET','POST'])
# @login_required
# def post_rating(post_id):
#   search_form=SearchForm()
#   post=Post.query.get_or_404(post_id)
#   rating_form=RatingForm()
#   if rating_form.validate_on_submit():
#     db.session.add(Rating(choice=rating_form.rating.data,post_id=post.id,rater_id=current_user.id))
#     db.session.commit()
#     flash("Your rating has been added to the post","success")
#     return redirect(f'/post/{post.id}')
#   ratings=Rating.query.filter(Rating.post_id==post.id)
#   return render_template('post.html',post=post, ratings=ratings, rating_form=rating_form,search_form=search_form)

# @app.route('/post/<int:post_id>/tag',methods=['GET','POST'])
# @login_required
# def post_tag(post_id):
#   search_form=SearchForm()
#   post=Post.query.get_or_404(post_id)
#   tag_form=TagForm()
#   tags = Tag.query.filter(and_(Tag.post_id==post.id, Tag.tagger_id==current_user.id))
#   tags_count = tags.count()
#   print(dir(tags))
#   if tag_form.validate_on_submit():
#     print(tags_count)
#     if tags_count==0:
#       db.session.add(Tag(post_id=post.id,tagger_id=current_user.id))
#       db.session.commit()
# #  Code for adding link to flask message adapted from https://stackoverflow.com/questions/21248718/how-to-flashing-a-message-with-link-using-flask-flash
# # accessed 06.2.2020, to my particular message and link
# # end of referenced code.
#       flash(Markup('Post has been added to your <a href="/user_account">tagged posts</a>'))
#       return redirect(f'/post/{post.id}')
#     flash(Markup('This post is already in your <a href="/user_account">tagged posts</a>'))
#     return  redirect(f'/post/{post.id}')
#   tags=Tag.query.filter(Tag.post_id==post.id)
#   return render_template('post.html',post=post, ratings=ratings, tag_form=tag_form,search_form=search_form)

# @app.route('/post/<int:post_id>/remove_tag',methods=['GET','POST'])
# @login_required
# def remove_tag(post_id):
#   search_form=SearchForm()
#   post=Post.query.get_or_404(post_id)
#   remove_tag_form=RemoveTagForm()
#   tags=Tag.query.filter(Tag.post_id==post.id)
#   if remove_tag_form.validate_on_submit():
#     Tag.query.filter_by(post_id=post_id).delete()
#     db.session.commit()
# #  Code for adding link to flask message adapted from https://stackoverflow.com/questions/21248718/how-to-flashing-a-message-with-link-using-flask-flash
# # accessed 06.2.2020, to my particular message and link
# # end of referenced code.
#     flash(Markup('Post has been removed from your <a href="/user_account">tagged posts</a>'))
#     return redirect(f'/post/{post.id}')
#   return render_template('post.html',post=post, ratings=ratings, remove_tag_form=remove_tag_form, tags=tags,search_form=search_form)

# @app.route('/post/search/<user_input>',methods=['GET', 'POST'])
# def search(user_input):
#   posts=Post.query.filter(or_(Post.title.contains(user_input), Post.content.contains(user_input)))
#   search_form=SearchForm()
#   sort_by_form=SortByForm()
#   if search_form.validate_on_submit():
#     x = search_form.user_input.data
#     return redirect(f'/post/search/{x}')
#   return render_template('allposts.html', posts=posts, search_form=search_form, sort_by_form=sort_by_form)

# @app.route("/allposts",methods=['GET', 'POST'])
# def allposts():
#   sort_by_form=SortByForm()
#   search_form=SearchForm()
#   if request.method == 'POST':
#     if sort_by_form.validate_on_submit():
#       a = sort_by_form.choice.data
#       if a == 'Date Descending':
# #  Code for ordering posts by date adapted from https://stackoverflow.com/questions/4582264/python-sqlalchemy-order-by-datetime
# # accessed 11.2.2020, adapted to my particular search parameters and database details
# # end of referenced code.
#         posts = Post.query.order_by(desc(Post.date)).all()
#       if a == 'Date Ascending':
#         posts = Post.query.order_by(Post.date).all()
#   else:
#     posts=Post.query.all()
#   return render_template('allposts.html', posts=posts, search_form=search_form, sort_by_form=sort_by_form)

