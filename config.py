import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1775@localhost:3306/pythonprueba'  # Base de datos real

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_database.db'  # Usar base de datos temporal
    TESTING = True
