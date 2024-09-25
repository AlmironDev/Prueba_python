from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definir el modelo de la tabla 'empresa'
class Empresa(db.Model):
    __tablename__ = 'empresa'
    id = db.Column(db.Integer, primary_key=True)  # Llave primaria
    nombre = db.Column(db.String(100), nullable=False)
    ruc = db.Column(db.BIGINT, nullable=False)

    # Relación con 'sectores'
    sectores = db.relationship('Sectores', backref='empresa', lazy=True)

# Definir el modelo de la tabla 'sectores'
class Sectores(db.Model):
    __tablename__ = 'sectores'
    id = db.Column(db.Integer, primary_key=True)  # Llave primaria
    id_empresa = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)  # Llave foránea a 'empresa'
    nombre = db.Column(db.String(100), nullable=False)

    # Relación con 'empleados'
    empleados = db.relationship('Empleado', backref='sector', lazy=True)

# Definir el modelo de la tabla 'empleados'
class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)  # Llave primaria
    id_sector = db.Column(db.Integer, db.ForeignKey('sectores.id'), nullable=True)  # Llave foránea a 'sectores'
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Float, nullable=False)

