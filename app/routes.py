from app import app
from flask import render_template

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
