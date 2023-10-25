from flask import Flask,render_template
import os

app = Flask(__name__)

#ruta principal 

@app.route("/")
def inicio():
    return render_template('index.html')

app.run(debug=True,port=4000)