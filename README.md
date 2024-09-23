# Prueba Tecnica Python

# Requerimientos que use

- Python 3.12.5

- | Flask | mysql-connector-python | matplotlib | pandas !

```sh
pip install -r requirements.txt
```

# Creacion base de datos

Hize un script para la creacion de la base de datos y mediante python poder ejecutarlo y cre

### Creacion de la base de datos | Uso | Creacion de la tabla | Inserccion de los datos | use requisistos python

```sh
CREATE SCHEMA pythonprueba;

use pythonprueba;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    ciudad VARCHAR(100),
    salario DECIMAL(10, 2)
);

INSERT INTO empleados (nombre, edad, ciudad, salario) VALUES
('Juan Perez', 28, 'Lima', 2500.00),
('Ana Gomez', 34, 'Arequipa', 3000.00),
('Luis Martinez', 45, 'Cusco', 4000.00),
('Maria Lopez', 30, 'Trujillo', 2800.50),
('Carlos Ruiz', 50, 'Piura', 3500.75);


```

## Usar Script

```sh
python create_db.py
```

## Inicializar

```sh
python conect_db_grafic.py
```

## Puerto expuesto

http://127.0.0.1:8000/ || http://localhost:8000/

# Como funciona

Primero nos conectamos a la base de datos de mysql mediante la libreria de mysql.connector , donde indicamos nuestras credenciales , despues ejecutamos el script para obtener todos los datos de los empleados , comvertimos los datos en DataFrames para asi generar las grafica de barras y circular , pero todo eso se hace cuando hacemos la llamada al puerto 8000 , donde por defecto se ejecutara esta funcion 

# Renderizar la plantilla con los datos y gráficos

Renderizamos en una plantilla ( / templates / index.html)

# Los graficos se guardaran en static

Los graficos generados mediante el script se guardaran( / static )
