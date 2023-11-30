from flask import Flask
from routes.routers import inicio_bp,login_bp,emple_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/proyecto1'
SQLALCHEMY_TRACK_NOTIFICATIONS = False

app.register_blueprint(inicio_bp)
app.register_blueprint(login_bp)
app.register_blueprint(emple_bp)

db = SQLAlchemy(app)

