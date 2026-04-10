from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db

from schemas.formacion import FormacionCreate, FormacionUpdate

from crud.formacion import (
    crear_formacion,
    listar_formacion,
    obtener_formacion_por_id,
    actualizar_formacion,
    eliminar_formacion
)

router = APIRouter(prefix="/formacion", tags=["Formacion"])


@router.post("/")
def crear(data: FormacionCreate, db: Session = Depends(get_db)):
    return crear_formacion(db, data)


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_formacion(db)


@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    data = obtener_formacion_por_id(db, id)
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data


@router.put("/{id}")
def actualizar(id: int, data: FormacionUpdate, db: Session = Depends(get_db)):
    obj = actualizar_formacion(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = eliminar_formacion(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return {"mensaje": "Eliminado"}