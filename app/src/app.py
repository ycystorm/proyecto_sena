from flask import Flask,render_template
import os
from  router import routers

app = Flask(__name__)

#importamos las rutas desde el archivo routers
app.register_blueprint(routers.inicio_bp)

if __name__ == "__main__":
    app.run(debug=True,port=4000)