
from flask import Flask
import os
from flask import render_template, Blueprint



run = Flask(__name__)


#ruta login

@run.route('/')
def login():
    return render_template('index.html')

@run.route('/login')
def log():
    return render_template('/login/login.html')

run.run(debug=True,port=4000)
