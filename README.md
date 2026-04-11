# Gestión de Personal y Formación

1. Información general
Nombre del proyecto: Servicio Web de Gestión de Personal y Formación
Integrantes: 
Juan Felipe Antury Bermeo
Juan David Restrepo Quintero
David Esteban Gaviria Chalarca
Asignatura: Aplicaciones y Servicios Web
Fecha: 11/04/2026

2. Descripción del sistema

Este proyecto consiste en el desarrollo de un servicio web utilizando FastAPI, que permite gestionar la información del personal de laboratorio y su formación académica y profesional.

El sistema implementa operaciones CRUD completas (Crear, Consultar, Actualizar y Eliminar) sobre dos entidades principales: Personal y Formación

El sistema está organizado en una arquitectura por capas:

models: Definición de tablas con SQLAlchemy
schemas: Validación de datos con Pydantic
crud: Lógica de acceso a datos
api: Definición de endpoints (routers)
db: Configuración de la base de datos

3. Configuración del entorno

Crear entorno virtual: 
python -m venv venv

Activar entorno:
-Windows: venv\Scripts\activate
-Linux/Mac: source venv/bin/activate

Instalar dependencias: pip install -r requirements.txt