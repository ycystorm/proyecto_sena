#dependencia de flask 
from flask import Flask
#Dependencia de configuración
from .config1 import Config
from config import vistas
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
#dependencia para las migraciones 
from flask_migrate import Migrate
from .router import routers

#crear el objeto python
app = Flask(__name__)

#Configuracion objeto flask
#app.config.from_object(Config)

#vincular blueprints del proyecto  
app = Flask(__name__, static_folder=vistas.STATIC_FOLDER, template_folder=vistas.TEMPALTE_FOLDER)


app.register_blueprint(routers.inicio_bp)
app.register_blueprint(routers.login_bp)

#Crear el objetto de Moldelos
#db = SQLAlchemy(app)

#Crear objeto de migración
#migrate = Migrate(app,db)

#importar los modelos
#from .models import Clientes,Empleado,Administrador,Informacion,Proyecto

