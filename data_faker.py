from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Generar datos falsos para 'Empresa'
def generar_empresas(cantidad):
    empresas = []
    for _ in range(cantidad):
        empresa = {
            "nombre": fake.company(),
            'ruc': fake.random_int(min=100000000, max=2147483647)  # Generar un RUC dentro del rango permitido
        }
        empresas.append(empresa)
    return empresas

# Generar datos falsos para 'Sectores'
def generar_sectores(cantidad, empresas_ids):
    sectores = []
    for _ in range(cantidad):
        sector = {
            "nombre": fake.job(),
            "id_empresa": random.choice(empresas_ids)
        }
        sectores.append(sector)
    return sectores

# Generar datos falsos para 'Empleados'
def generar_empleados(cantidad, sectores_ids):
    empleados = []
    for _ in range(cantidad):
        empleado = {
            "nombre": fake.name(),
            "edad": random.randint(20, 60),
            "ciudad": fake.city(),
            "salario": round(random.uniform(2000, 5000), 2),
            "id_sector": random.choice(sectores_ids)
        }
        empleados.append(empleado)
    return empleados
