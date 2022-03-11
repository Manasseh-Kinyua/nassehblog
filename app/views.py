from flask import render_template
from app import app

@app.route('/')
def index():
    title = 'Home: Welcome to my blog'
    return render_template('index.html', title = title)

@app.route('/about')
def about():
    title = 'Home: Welcome to my blog'
    return render_template('about.html', title = title)