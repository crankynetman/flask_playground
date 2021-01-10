from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris Cummings'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Chicago!'
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user "{form.username.data}" with password "{form.password.data}", and remember_me set to "{form.remember_me.data}"')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
