import unittest
import os
from models import db, Empresa, Sectores, Empleado
from data_faker import generar_empresas, generar_sectores, generar_empleados
from config import TestingConfig

os.environ['TESTING'] = '1'
from app import app
class FlaskAppTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Configuración inicial para las pruebas."""
        # Establecer variable de entorno para modo prueba
        os.environ['TESTING'] = '1'
        print("poniendo variable testing")
        cls.app = app
        cls.app.config.from_object(TestingConfig)  # Cargar configuración de pruebas
        cls.client = cls.app.test_client()

        with cls.app.app_context():
            # Imprimir la base de datos que se está utilizando
            db_uri = cls.app.config['SQLALCHEMY_DATABASE_URI']
            print(f"Usando base de datos: {db_uri}")  # Mensaje de depuración
            
            db.create_all()  # Crear las tablas para las pruebas

    @classmethod
    def tearDownClass(cls):
        """Limpiar la base de datos después de las pruebas."""

        # Eliminar el archivo de la base de datos de pruebas
        if os.path.exists('test_database.db'):
            os.remove('test_database.db')

    def test_generar_datos(self):
        """Prueba para verificar la generación de datos falsos."""
        with self.app.app_context():
            response = self.client.get('/generar_datos')
            self.assertEqual(response.data.decode(), "Datos falsos generados e insertados con éxito.")
            
            # Verificar que se hayan insertado datos
            empresas = Empresa.query.all()
            self.assertGreater(len(empresas), 0)

            sectores = Sectores.query.all()
            self.assertGreater(len(sectores), 0)

    def test_index(self):
        """Prueba para verificar que la página principal se carga correctamente."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
