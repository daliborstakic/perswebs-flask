from flask import render_template
from perswebs import app

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/about')
def About():
    return render_template('about.html', title='About')
