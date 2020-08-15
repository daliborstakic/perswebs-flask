from flask import render_template
from perswebs import app

# Main page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

# About page
@app.route('/about')
def about():
    return render_template('about.html', title='About')
