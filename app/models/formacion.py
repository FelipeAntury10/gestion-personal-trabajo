from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db import Base

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema":"grupo_1"}

    idFormacion = Column(Integer, primary_key=True, index=True)
    idPersona = Column(
        Integer,
        ForeignKey("grupo_1.personal.idPersona"),
        nullable=False
    )
    nivelDeFormacion = Column(String(50), nullable=False)
    tituloObtenido = Column(String(100), nullable=False)
    institucion = Column(String(100), nullable=False)
    fechaFinal = Column(Date, nullable=False)