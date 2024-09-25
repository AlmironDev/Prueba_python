from flask import Flask, render_template
from flask_migrate import Migrate
import matplotlib.pyplot as plt
import pandas as pd
import os

from data_faker import generar_empresas, generar_sectores, generar_empleados
from config import Config, TestingConfig
from models import db, Empresa, Sectores, Empleado  # Importar db aquí

# Inicializar la aplicación
app = Flask(__name__)

# Cargar configuración según el entorno

if os.getenv('TESTING') == '1':
    print("Entrando al modo de testing")
    app.config.from_object(TestingConfig)
else:
    print("Entrando al modo de base de datos")
    app.config.from_object(Config)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos y las migraciones
db.init_app(app)  # Inicializar db con la app
migrate = Migrate(app, db)

# Rutas y lógica de la aplicación
@app.route("/")
def index():
    empleados = Empleado.query.all()

    # Convertir los resultados a un DataFrame
    df = pd.DataFrame([(e.id, e.nombre, e.edad, e.ciudad, e.salario) for e in empleados], 
                      columns=["id", "nombre", "edad", "ciudad", "salario"])

    # Gráfico de barras: Edad vs Salario
    plt.figure(figsize=(10, 5))
    plt.bar(df['edad'], df['salario'])
    plt.title('Relación entre Edad y Salario')
    plt.xlabel('Edad')
    plt.ylabel('Salario')
    plt.savefig('static/edad_salario.png')
    plt.close()

    # Gráfico circular: Cantidad de personas por ciudad
    ciudad_counts = df['ciudad'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(ciudad_counts, labels=ciudad_counts.index, autopct='%1.1f%%')
    plt.title('Cantidad de Personas por Ciudad')
    plt.savefig('static/personas_por_ciudad.png')
    plt.close()

    # Renderizar la plantilla con los datos y gráficos
    return render_template("index.html", data=df.to_dict(orient='records'))

@app.route('/generar_datos')
def generar_datos():
    # Generar empresas, sectores y empleados falsos
    empresas_falsas = generar_empresas(5)
    sectores_falsos = generar_sectores(10, [1, 2, 3, 4, 5])
    empleados_falsos = generar_empleados(20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Insertar empresas en la base de datos
    for empresa in empresas_falsas:
        nueva_empresa = Empresa(**empresa)
        db.session.add(nueva_empresa)

    for sector in sectores_falsos:
        nuevo_sector = Sectores(**sector)
        db.session.add(nuevo_sector)

    for empleado in empleados_falsos:
        nuevo_empleado = Empleado(**empleado)
        db.session.add(nuevo_empleado)

    db.session.commit()

    return "Datos falsos generados e insertados con éxito."

if __name__ == "__main__":
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, port=8000)
