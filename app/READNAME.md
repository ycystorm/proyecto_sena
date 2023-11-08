
para crear la carpeta del entorno virtual
python -m virtualenv venv

para activar el entorno virtual
.\venv\Scripts\activate

para crear el archivo requirements.txt o actualizarlo
pip freeze > requirements.txt

version utilizada de python es la 11.5

comandos para jecutar la migracion 
flask db init 


flask db migrate -m"comentario de la migracion"

flask db upgrade

