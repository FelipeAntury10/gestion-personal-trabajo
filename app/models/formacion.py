from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db import Base, SCHEMA_NAME

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": SCHEMA_NAME}

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(
        Integer,
        ForeignKey(f"{SCHEMA_NAME}.personal.idPersona"),
        nullable=False
    )
    nivelDeFormacion = Column(String(50), nullable=False)
    tituloObtenido = Column(String(100), nullable=False)
    institucion = Column(String(100), nullable=False)
    fechaFinal = Column(Date, nullable=False)