from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class Personal(Base):
    __tablename__ = "personal"
    __table_args__ = {"schema":"grupo_1"}

    idPersona = Column(Integer, primary_key=True, index=True)
    idCargo = Column(Integer, nullable=False)
    nombre = Column(String(50), nullable=False)
    documento = Column(String(50), unique=True, nullable=False)
    correo = Column(String(50), unique=True, nullable=False)
    telefono = Column(String(50), nullable=True)
    estado = Column(Boolean, default=True)