from flask import Flask, render_template
import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd
import os

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1775',
        database='pythonprueba'
    )
    return conn

# Ruta para la página principal
@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados a un DataFrame para facilitar la visualización
    df = pd.DataFrame(resultados, columns=["id", "nombre", "edad", "ciudad", "salario"])

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

if __name__ == "__main__":
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, port=8000)
