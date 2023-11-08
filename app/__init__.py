from flask import Flask
#importacion de los blueprint
from .router import routers
from config import vistas
#Dependencia de configuración de la base de datos
from .database.mysql_db import Config
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



#crear el objeto python
app = Flask(__name__)

#Configuracion objeto flask mi conexion a base de datos
app.config.from_object(Config)


app = Flask(__name__, static_folder=vistas.STATIC_FOLDER, template_folder=vistas.TEMPALTE_FOLDER)

#importamos las rutas desde el archivo routers
app.register_blueprint(routers.inicio_bp)
app.register_blueprint(routers.login_bp)


#Crear el objetto de Moldelos
db = SQLAlchemy(app)


#Crear objeto de migración
migrate = Migrate(app,db)


#importar los omodelos
from database.migrationsModel import Clientes,Empleado,Administrador,Informacion,Proyecto


