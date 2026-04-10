from fastapi import FastAPI
from app.db import engine, Base
from app.models import personal, formacion  # noqa
from appapi.personal import router as personal_router
from appapi.formacion import router as formacion_router

app = FastAPI(
    title="API Gestión de Personal y Formación",
    description="Servicio web para la gestión del personal de laboratorios y su formación académica.",
    version="1.0.0",
)

app.include_router(personal_router)
app.include_router(formacion_router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}
