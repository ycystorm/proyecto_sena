#dependencia de flask 
from flask import Flask
#Dependencia de configuración
#from .config1 import Config
from config import vistas
#dependencia para las migraciones 
from flask_migrate import Migrate
from .routes.routers import inicio_bp,login_bp,emple_bp
from .utils.db import db 

#crear el objeto python
app = Flask(__name__)



#vincular blueprints del proyecto  
app = Flask(__name__, static_folder=vistas.STATIC_FOLDER, template_folder=vistas.TEMPALTE_FOLDER)


app.register_blueprint(inicio_bp)
app.register_blueprint(login_bp)
app.register_blueprint(emple_bp)

#Crear objeto de migración
migrate = Migrate(app,db)

#importar los modelos
from .model.models import Clientes,Empleado,Administrador,Proyecto,Usuarios,servicios

