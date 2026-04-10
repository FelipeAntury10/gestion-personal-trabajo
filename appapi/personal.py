from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db

from schemas.personal import PersonalCreate, PersonalUpdate

from crud.personal import (
    crear_personal,
    listar_personal,
    obtener_personal_por_id,
    actualizar_personal,
    eliminar_personal
)

router = APIRouter(prefix="/personal", tags=["Personal"])


@router.post("/")
def crear(data: PersonalCreate, db: Session = Depends(get_db)):
    return crear_personal(db, data)


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_personal(db)


@router.get("/{id}")
def obtener(id: int, db: Session = Depends(get_db)):
    data = obtener_personal_por_id(db, id)
    if not data:
        raise HTTPException(status_code=404, detail="No encontrado")
    return data


@router.put("/{id}")
def actualizar(id: int, data: PersonalUpdate, db: Session = Depends(get_db)):
    obj = actualizar_personal(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return obj


@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    obj = eliminar_personal(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="No encontrado")
    return {"mensaje": "Eliminado"}