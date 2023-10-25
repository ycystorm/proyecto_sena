import mysql.connector
#creamos la conexion

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="laboratoriosql"
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as error:
        print(f'Error al conectar a la base de datos: {error}')
        return None