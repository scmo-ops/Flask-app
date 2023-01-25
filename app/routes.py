from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index(): 
    user = {'username' : 'Miguel'} # right now, since I don't have the usernames and their posts; I creted them to focus on rendering and building the blog first.
    posts = [
        {
            'author':{'username':'Jhon'},
            'body': 'I need to learn statisctics, advanced math, and advanced sql and python '
        },
        {
            'author': {'username':'Susan'},
            'body': 'Im Skyler white yo'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title= 'Sign In', form=form) #here form=form means that I'm passing the form object created in the line above to the template
#with the name from. This is requiered to get the form fields rendered.