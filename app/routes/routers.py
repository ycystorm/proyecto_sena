from flask import Flask,render_template
import os
from flask import  Blueprint
from ..utils.db import db
#se crea un blueprint para la ruta de inicio 
inicio_bp = Blueprint('home',__name__)
#se crea un blueprint para la ruta de login
login_bp = Blueprint('login',__name__) 

emple_bp = Blueprint('indexE', __name__)

#ruta de inicio
@inicio_bp.route('/')
def index():
        return render_template('index.html')

#ruta de login
@login_bp.route('/login')
def login():
        return render_template('/login/login.html')
@login_bp.route('/registro')
def register():
        return render_template('/login/register.html')


@emple_bp.route('/menuEmpleado')
def menuE():
        return render_template('/empleado/menuE.html')





