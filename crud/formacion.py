from sqlalchemy.orm import Session
from app.models.formacion import Formacion
from app.schemas.formacion import FormacionCreate, FormacionUpdate


# 🔹 Crear un nuevo registro
def crear_formacion(db: Session, formacion: FormacionCreate):
    nueva_formacion = Formacion(**formacion.dict())
    db.add(nueva_formacion)
    db.commit()
    db.refresh(nueva_formacion)
    return nueva_formacion


# 🔹 Listar todos los registros
def listar_formacion(db: Session):
    return db.query(Formacion).all()


# 🔹 Consultar un registro por ID
def obtener_formacion_por_id(db: Session, id_formacion: int):
    return db.query(Formacion).filter(Formacion.idFormacion == id_formacion).first()


# 🔹 Actualizar un registro existente
def actualizar_formacion(db: Session, id_formacion: int, formacion: FormacionUpdate):
    db_formacion = obtener_formacion_por_id(db, id_formacion)
    if not db_formacion:
        return None

    for key, value in formacion.dict(exclude_unset=True).items():
        setattr(db_formacion, key, value)

    db.commit()
    db.refresh(db_formacion)
    return db_formacion


# 🔹 Eliminar un registro
def eliminar_formacion(db: Session, id_formacion: int):
    db_formacion = obtener_formacion_por_id(db, id_formacion)
    if not db_formacion:
        return None

    db.delete(db_formacion)
    db.commit()
    return db_formacion