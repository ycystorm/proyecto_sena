class Config:
    #definir 'cadena de conexion (conectionstring)'
    SQLALCHEMY_DATABASE_URI='mysql://root:@localhost/proyecto'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'jean'