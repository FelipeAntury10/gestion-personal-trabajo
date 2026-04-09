from fastapi import FastAPI

app = FastAPI(
    title="API Gestión de Personal y Formación",
    description="Servicio web para la gestión del personal de laboratorios y su formación académica.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}