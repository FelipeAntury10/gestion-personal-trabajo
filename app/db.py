import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
SCHEMA_NAME = os.getenv("SCHEMA_NAME")

# Validación básica
if not DATABASE_URL:
    raise ValueError("La variable DATABASE_URL no está definida en el archivo .env")

if not SCHEMA_NAME:
    raise ValueError("La variable SCHEMA_NAME no está definida en el archivo .env")

# Crear el motor de conexión a PostgreSQL
engine = create_engine(DATABASE_URL)

# Crear la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos ORM
Base = declarative_base()

# Función para inyección de dependencias en FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()