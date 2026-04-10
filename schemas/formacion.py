from pydantic import BaseModel
from typing import Optional
from datetime import date

# 🔹 Esquema para crear un nuevo registro
class FormacionCreate(BaseModel):
    idPersona: int
    nivelDeFormacion: str
    tituloObtenido: str
    institucion: str
    fechaFinal: date


# 🔹 Esquema para actualizar un registro existente
class FormacionUpdate(BaseModel):
    idPersona: Optional[int] = None
    nivelDeFormacion: Optional[str] = None
    tituloObtenido: Optional[str] = None
    institucion: Optional[str] = None
    fechaFinal: Optional[date] = None


# 🔹 Esquema para la salida de datos
class FormacionOut(BaseModel):
    idFormacion: int
    idPersona: int
    nivelDeFormacion: str
    tituloObtenido: str
    institucion: str
    fechaFinal: date

    class Config:
        from_attributes = True  # Compatible con Pydantic v2