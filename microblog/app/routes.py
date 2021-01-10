from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris Cummings'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie exists and I have no opinion on the quality of the film!'
        },
        {
            'author': {'username': 'Sarah'},
            'body': 'This is a message.'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
