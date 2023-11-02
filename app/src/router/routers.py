
from flask import Flask,render_template
import os
from flask import  Blueprint

app = Flask(__name__)

#se crea un blueprint para la ruta de inicio 
inicio_bp = Blueprint('home',__name__)

#ruta de inicio
@inicio_bp.route('/')
def index():
        return render_template('index.html')


#agragamos el blueprint a la palicacion
app.register_blueprint(inicio_bp)

# Iniciamos el servidor web
if __name__ == '__main__':
    app.run()
