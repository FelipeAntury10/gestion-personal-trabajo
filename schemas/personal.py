from pydantic import BaseModel, EmailStr
from typing import Optional

# 🔹 Esquema para crear un nuevo registro
class PersonalCreate(BaseModel):
    idCargo: int
    nombre: str
    documento: str
    correo: EmailStr
    telefono: Optional[str] = None
    estado: Optional[bool] = True


# 🔹 Esquema para actualizar un registro existente
class PersonalUpdate(BaseModel):
    idCargo: Optional[int] = None
    nombre: Optional[str] = None
    documento: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    estado: Optional[bool] = None


# 🔹 Esquema para la salida de datos
class PersonalOut(BaseModel):
    idPersona: int
    idCargo: int
    nombre: str
    documento: str
    correo: EmailStr
    telefono: Optional[str]
    estado: bool

    class Config:
        from_attributes = True  # Compatible con Pydantic v2