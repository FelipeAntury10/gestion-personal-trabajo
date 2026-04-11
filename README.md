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

Este proyecto consiste en el desarrollo de un servicio web utilizando FastAPI para la gestión del personal de laboratorios y su formación académica y profesional.

El sistema permite realizar operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) sobre dos entidades principales: Personal y Formación

La información se almacena de forma persistente en una base de datos PostgreSQL, garantizando su disponibilidad y consistencia.

El proyecto está organizado siguiendo una arquitectura por capas:

app/
  main.py: punto de entrada de la aplicación
  db.py: configuración de la base de datos
  models/: modelos SQLAlchemy
schemas/: validación de datos con Pydantic
crud/: lógica de acceso a datos
appapi/: definición de endpoints (routers)

Esta estructura permite mantener el código modular, escalable y fácil de mantener.


3. Configuración del entorno
- Crear entorno virtual: python -m venv venv
- Activar entorno:
   Windows: venv\Scripts\activate
   Linux/Mac: source venv/bin/activate
- Instalar dependencias: pip install -r requirements.txt


4. Configuración de la base de datos

El sistema utiliza PostgreSQL como base de datos y maneja las credenciales mediante variables de entorno.
Archivo .env

Crear un archivo .env en la raíz del proyecto:

DATABASE_URL=postgresql://admin:admin@190.248.28.132:3010/dbapps
SCHEMA_NAME=grupo_1

Importante:

No subir este archivo al repositorio
Está incluido en .gitignore

Configuración técnica
- ORM utilizado: SQLAlchemy
- Validación de datos: Pydantic
- Inyección de dependencias: get_db()
- Creación automática de tablas: Base.metadata.create_all(bind=engine)


5. Ejecución del proyecto
 - Ejecutar servidor: uvicorn app.main:app --reload
 - Acceso:
     API: http://127.0.0.1:8000
     Swagger: http://127.0.0.1:8000/docs


6. Endpoints implementados
 - Personal
     POST /personal → Crear registro
     GET /personal → Listar registros
     GET /personal/{id} → Consultar por ID
     PUT /personal/{id} → Actualizar
     DELETE /personal/{id} → Eliminar

 - Formación
     POST /formacion → Crear registro
     GET /formacion → Listar registros
     GET /formacion/{id} → Consultar por ID
     PUT /formacion/{id} → Actualizar
     DELETE /formacion/{id} → Eliminar


7. Evidencias de funcionamiento 

- ejecución del servidor: 

![servidor](./imagenes/terminal.png)
![swagger](./imagenes/captura1.png)
![POST de personal](./imagenes/post.png)
![GET de personal](./imagenes/get.png)
![PUT de personal](./imagenes/put1.png)
![PUT de personal](imagenes/put2.png)
![DELETE de personal](./imagenes/delete.png)
![evidencia Postgre Post](./imagenes/evidenciaPost1.png)
![evidencia Postgre Delete](./imagenes/evidenciaDatosBorrados.png)


8. Control de versiones
 Repositorio GitHub: https://github.com/FelipeAntury10/gestion-personal-trabajo.git

Aportes del equipo
Integrante 1: Completando CRUD y endpoints, completando y mejorando código
835d3f108a73b98473d5930993de35c87d8d79bb
f87427260a813db67a7122337cc56c4192a2370e

Integrante 2: Modelos y schemas, configuación de bases de datod
d24808e08eff67e388933e9ac53005208f1a7786
d42a2a7f84c552654d4fbd23dd8d79cb14cca52d
3596be995d95c3337e22218d3cb7e29d7498a9f1

Integrante 3: Completando detalles de código y readme
a29443c32c2b6d74d4b6347d62a06c6ed09c72d8
f833eea9d3cf4f25eb411e106cee75fba9e11afc
e38e8f791a7d4a7a6733d2995f6ac022b881d3a8

9. Conclusiones

Durante el desarrollo del proyecto se logró:

- Implementar un servicio web con FastAPI
- Aplicar arquitectura por capas
- Conectar a PostgreSQL usando SQLAlchemy
- Utilizar variables de entorno para seguridad
- Implementar operaciones CRUD completas

Dificultades:
- Configuración de conexión a la base de datos
- Manejo de variables de entorno
- Organización modular del proyecto

Soluciones:
- Uso de archivo .env
- Separación clara de responsabilidades
- Pruebas constantes con Swagger