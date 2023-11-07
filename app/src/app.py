from flask import Flask, after_app_request
from router import routers
#Dependencia de configuración de la base de datos
from database.mysql_db import Config
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

#Configuracion objeto flask
app.config.from_object(Config)



#importamos las rutas desde el archivo routers
app.register_blueprint(routers.inicio_bp)
app.register_blueprint(routers.login_bp)


#Crear el objetto de Moldelos
db = SQLAlchemy(app)


#Crear objeto de migración
migrate = Migrate(app, db)

# Carga el modelo de migraciones
#from database.migrationsModel import Clientes, Empleado, Administrador, Proyecto, Informacion

# Define un manejador para el evento app_initialized


if __name__ == "__main__":
    app.run(debug=True,port=4000)