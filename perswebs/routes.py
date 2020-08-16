from flask import render_template
from perswebs import app

# Main page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
