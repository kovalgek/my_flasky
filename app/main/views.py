from flask import  render_template
from . import main

@main.route('/', methods = ['GET', 'POST'])
def index():
    #from = NameForm()
    return render_template('index.html')