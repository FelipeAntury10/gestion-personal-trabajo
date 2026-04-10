from sqlalchemy.orm import Session
from app.models.personal import Personal
from schemas.personal import PersonalCreate, PersonalUpdate


# 🔹 Crear un nuevo registro
def crear_personal(db: Session, personal: PersonalCreate):
    nuevo_personal = Personal(**personal.dict())
    db.add(nuevo_personal)
    db.commit()
    db.refresh(nuevo_personal)
    return nuevo_personal


# 🔹 Listar todos los registros
def listar_personal(db: Session):
    return db.query(Personal).all()


# 🔹 Consultar un registro por ID
def obtener_personal_por_id(db: Session, id_persona: int):
    return db.query(Personal).filter(Personal.idPersona == id_persona).first()


# 🔹 Actualizar un registro existente
def actualizar_personal(db: Session, id_persona: int, personal: PersonalUpdate):
    db_personal = obtener_personal_por_id(db, id_persona)
    if not db_personal:
        return None

    for key, value in personal.dict(exclude_unset=True).items():
        setattr(db_personal, key, value)

    db.commit()
    db.refresh(db_personal)
    return db_personal


# 🔹 Eliminar un registro
def eliminar_personal(db: Session, id_persona: int):
    db_personal = obtener_personal_por_id(db, id_persona)
    if not db_personal:
        return None

    db.delete(db_personal)
    db.commit()
    return db_personal