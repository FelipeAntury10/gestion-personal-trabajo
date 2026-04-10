from fastapi import FastAPI
from app.db import engine, Base

# Importar los modelos para que sean registrados en la metadata
from app.models import personal, formacion  # noqa

app = FastAPI(
    title="API Gestión de Personal y Formación",
    description="Servicio web para la gestión del personal de laboratorios y su formación académica.",
    version="1.0.0"
)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}