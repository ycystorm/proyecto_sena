
from flask import Flask,render_template
import os
from flask import  Blueprint


app = Flask(__name__)

#se crea un blueprint para la ruta de inicio 
inicio_bp = Blueprint('home',__name__)
#se crea un blueprint para la ruta de login
login_bp = Blueprint('login',__name__) 

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

#agragamos el blueprint a la palicacion
app.register_blueprint(inicio_bp)
app.register_blueprint(login_bp)

# Iniciamos el servidor web
if __name__ == '__main__':
    app.run()
