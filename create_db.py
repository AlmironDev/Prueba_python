import mysql.connector

# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1775',
)

# Crear un cursor para ejecutar comandos
cursor = conexion.cursor()

# Leer el archivo script.sql
with open('script.sql', 'r') as archivo_sql:
    script_sql = archivo_sql.read()

# Ejecutar el script SQL
try:
    # Dividir el script por comandos y eliminar líneas vacías
    comandos = [comando.strip() for comando in script_sql.split(';') if comando.strip()]
    
    for comando in comandos:
        cursor.execute(comando)
    
    # Hacer commit de los cambios
    conexion.commit()
    
    print("Script SQL ejecutado correctamente.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Cerrar la conexión
    cursor.close()
    conexion.close()
