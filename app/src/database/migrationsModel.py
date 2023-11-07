from app import db
from sqlalchemy import Column, Integer, String, Date, Enum, BLOB, Boolean, null



class Clientes(db.Model):
    __tablename__ = "clientes"
    ID_del_cliente = Column(Integer,primary_key=True)
    Nombre_del_cliente = Column(String(50))
    apellido_del_cliente = Column(String(50))
    Correo_electrónico_del_cliente = Column(String(50))
    Dirección_del_cliente = Column(String(50))
    telefono_cliente = Column(Integer(15))
    Fecha_de_nacimiento = Column(Date)
    Género_del_cliente = Column(Enum("masculino", "femenino"))
    numero_de_telefono_cliente = Column(Integer(30))
    foto_De_perfil_client = Column(BLOB)
    contraseña_cliente = Column(String(16))
    
class Administrador(db.Model):
    __tablename__ = "administrador"
    ID_del_administrador = Column(Integer,primary_key=True)
    Nombre_del_administrador = Column(String(50))
    apellido_del_administrador = Column(String(50))
    Correo_electrónico_del_administrador = Column(String(50))
    Dirección_del_administrador = Column(String(50))
    Teléfono_del_administrador = Column(Integer(15))
    Fecha_de_nacimiento =  Column(Date)
    Género_del_administrador = Column(Enum("masculino", "femenino"))
    numero_de_telefono_fijo_administrador = Column(Integer(10))
    foto_De_perfil_administrador = Column(BLOB)
    contraseña_administrador = Column(String(16))
    eps = Column(String(50))
    
class Empleado(db.Model):
    __tablename = "empleado"
    ID_del_empleado = Column(Integer,primary_key=True)
    Nombre_del_empleado = Column(String(50))
    apellido_del_empleado = Column(String(50))
    Correo_electrónico_del_empleado = Column(String(50))
    permiso_empleado = Column(Enum("si", "no"))
    Dirección_del_empleado = Column(String(50))
    Teléfono_del_empleado =Column(Integer(15))
    Fecha_de_empleado = Column(Date)
    Género_del_empleado = Column(Enum("masculino", "femenino"))
    numero_de_telefono_fijo_empleado = Column(Integer(10))
    foto_De_perfil_empleado = Column(BLOB)
    contraseña_empleado = Column(String(16))
    eps = Column(String(50))
    
class Proyecto(db.Model):
    __tablename__= "proyectos"
    
    id_proyecto = Column(Integer,primary_key=True)
    nombre_Del_proyecto = Column(String(50))
    nombre_del_cliente_de_proyecto = Column(String(50))
    nombre_empleados_participantes_proyecto = Column(String(50))
    descripcion_del_proyecto = Column(String(250))
    material_necesitado_del_proyecto = Column(String(250))

class Informacion(db.Model):
    __tablename__ = "informacion_general"
    id_info = Column(Integer,primary_key=True)
    foto_info = Column(String(50))
    descripcion_info = Column(String(250))
    nombre_info = Column(String(50))
    


