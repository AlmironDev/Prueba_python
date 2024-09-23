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
