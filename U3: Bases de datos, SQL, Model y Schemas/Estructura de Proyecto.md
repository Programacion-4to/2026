# Estructura de Proyecto: Schemas, Models y DTOs (Python + Pydantic)

## Teoría: las 3 capas

Schemas, Models y DTOs son **tres capas distintas** que representan los datos en diferentes momentos de su ciclo de vida. Cada una tiene una responsabilidad clara.

### Forma corta de recordarlo

- **Schema** → habla con el **cliente** (HTTP).
- **Model** → habla con la **base de datos** (SQL).
- **DTO** → habla **entre las capas** de tu app (Python ↔ Python).

Cada uno protege a las otras dos capas de cambios: si cambia la BD, el schema no se entera; si cambia la API, el model no se entera; el DTO los desacopla.

```
   ┌──────────────┐         ┌──────────────┐         ┌──────────────┐
   │   SCHEMA     │         │     DTO      │         │    MODEL     │
   │  (Pydantic)  │         │  (Pydantic)  │         │ (SQLAlchemy) │
   ├──────────────┤         ├──────────────┤         ├──────────────┤
   │ contrato     │         │ contrato     │         │ contrato     │
   │ con el       │         │ entre        │         │ con la       │
   │ CLIENTE      │         │ CAPAS        │         │ BASE DE DATOS│
   ├──────────────┤         ├──────────────┤         ├──────────────┤
   │ valida       │         │ transporta   │         │ persiste     │
   │ JSON entrante│         │ datos        │         │ filas        │
   └──────┬───────┘         └──────┬───────┘         └──────┬───────┘
          │                        │                        │
          ▼                        ▼                        ▼
       Routers              Services / Repos           Repositorio
```

---

### 1. Schema (capa de validación / entrada-salida)

Es la **definición de la forma** que deben tener los datos que **entran o salen** de tu API. Validan tipo, formato, longitud, requeridos, etc.

- **Dónde vive**: en la frontera HTTP (routers).
- **Qué hace**: valida el `body`, `query`, `path params`, antes de que toque la lógica.
- **Herramienta**: **Pydantic** (en Python). En FastAPI, los schemas se usan directamente como tipo del parámetro y FastAPI valida automáticamente.
- **No conoce la base de datos.** Solo describe el contrato externo.

```python
# schemas/user_schema.py
from pydantic import BaseModel, EmailStr, Field

class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(ge=18)

class UpdateUserSchema(BaseModel):
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8)
    age: int | None = Field(default=None, ge=18)
```

---

### 2. Model (capa de persistencia)

Es la **representación del dato en la base de datos**. Mapea tabla a clase.

- **Dónde vive**: cerca del repositorio / ORM.
- **Qué hace**: define columnas, relaciones, índices, constraints.
- **Herramientas típicas**: SQLAlchemy, SQLModel, Tortoise ORM, Peewee.
- **Contiene campos sensibles** (password hash, tokens, flags internos) que **nunca** deberían salir tal cual al cliente.

```python
# db/models/user_model.py (SQLAlchemy)
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from db.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)   # nunca se expone
    age = Column(Integer, nullable=False)
    is_admin = Column(Boolean, default=False)        # nunca se expone
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
```

---

### 3. DTO (Data Transfer Object)

Es el **objeto que viaja entre capas** (router → service → repo, o service → cliente). Es un "contenedor de datos limpio".

En Python con Pydantic, los DTOs también se modelan con `BaseModel`. La diferencia con un schema es **el rol**, no la herramienta:

- **Input DTO**: lo que el service espera recibir (ya validado).
- **Output DTO / Response DTO**: lo que devolvés al cliente (sin password, sin flags internos).

```python
# dtos/user_dto.py
from pydantic import BaseModel
from datetime import datetime

class CreateUserDTO(BaseModel):
    email: str
    password: str
    age: int

class UserResponseDTO(BaseModel):
    id: int
    email: str
    age: int
    created_at: datetime

    model_config = {"from_attributes": True}  # permite construirlo desde un Model SQLAlchemy
```

> Nota: en proyectos chicos con FastAPI muchas veces el `Schema` y el `DTO` se fusionan en una misma clase Pydantic. Mantenerlos separados es útil cuando el contrato HTTP y el contrato interno divergen.

---

### 4. Router (capa de exposición HTTP)

Es la **puerta de entrada** de tu API. Define **qué endpoints existen**, qué método HTTP los activa (`GET`, `POST`, etc.), qué schema valida la entrada y qué DTO se devuelve.

- **Dónde vive**: en `routers/`. Cada dominio (users, products) suele tener su propio router.
- **Qué hace**:
  1. Declara la URL y el verbo HTTP.
  2. Recibe el request y lo deja que FastAPI lo valide contra un Schema.
  3. Inyecta dependencias (sesión de BD, usuario autenticado).
  4. Llama al `service` con el DTO correspondiente.
  5. Devuelve la respuesta tipada con un `response_model` (DTO).
- **Qué NO hace**:
  - No tiene lógica de negocio (eso es del service).
  - No hace queries a la BD (eso es del repository).
  - No transforma datos complejos (eso es del mapper).
- **Herramienta**: `APIRouter` de FastAPI (en Express sería `Router`, en Flask sería `Blueprint`).

```python
# routers/user_router.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.connection import get_db
from schemas.user_schema import CreateUserSchema
from dtos.user_dto import CreateUserDTO, UserResponseDTO
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def create_user(payload: CreateUserSchema, db: Session = Depends(get_db)):
    # FastAPI ya validó el body contra CreateUserSchema
    dto = CreateUserDTO(**payload.model_dump())
    return UserService(db).create(dto)

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_by_id(user_id)
```

**Diferencia router vs controller**: en frameworks como Express se separa el `router` (URLs) del `controller` (función que maneja la request). En FastAPI suelen estar fusionados: la función decorada con `@router.post` cumple ambos roles.

---

## Diferencias entre Schema, DTO y Model

Ahora que vimos cada capa por separado, queda claro qué las distingue.

### DTO vs Schema

Ambos en Python se escriben con `BaseModel` de Pydantic, pero tienen **roles distintos**:

| | **Schema** | **DTO** |
|---|---|---|
| **Para qué sirve** | Validar datos que entran/salen por HTTP | Transportar datos entre capas internas (router → service → repo) |
| **Dónde vive** | En la frontera de la API (routers) | En toda la app, principalmente entre service y repository |
| **Quién lo usa** | FastAPI lo usa automáticamente al recibir el request | Lo usa el código de tu lógica de negocio |
| **Qué representa** | El **contrato HTTP** (lo que el cliente puede mandar/recibir) | El **contrato interno** (lo que tu service necesita o devuelve) |
| **Ejemplo de campo** | `password: str` (lo que manda el cliente) | `password_hash: str` (lo que el service ya hasheó) |
| **Si cambia la API** | Cambia el schema | El DTO puede quedarse igual |

```python
# Schema: lo que llega del cliente
class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str       # texto plano
    age: int

# DTO: lo que viaja hacia el repository
class CreateUserDTO(BaseModel):
    email: str
    password_hash: str  # ya hasheado por el service
    age: int
```

> En proyectos chicos suelen fusionarse en una sola clase. Se separan cuando el contrato HTTP y el contrato interno divergen.

### Model vs Schema

Acá la diferencia es **mucho más clara** porque usan herramientas distintas:

| | **Model** | **Schema** |
|---|---|---|
| **Para qué sirve** | Representar una **tabla** de la base de datos | Validar datos de entrada/salida HTTP |
| **Herramienta** | ORM (SQLAlchemy, SQLModel, Tortoise) | Pydantic |
| **Sabe de la BD** | Sí: columnas, tipos SQL, relaciones, índices | No, ni se entera |
| **Sabe de HTTP** | No | Sí (es el contrato del endpoint) |
| **Tiene campos sensibles** | Sí: `password_hash`, `is_admin`, `deleted_at` | No, se filtran antes de devolver |
| **Persiste datos** | Sí, lo guarda el ORM | No, es solo validación en memoria |
| **Si cambia la BD** | Hay que cambiarlo (y migrar) | No necesariamente |
| **Si cambia la API** | No se toca | Hay que cambiarlo |

```python
# Model: SQLAlchemy, mapea a la tabla "users"
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password_hash = Column(String)   # campo interno
    is_admin = Column(Boolean)       # campo interno

# Schema: Pydantic, valida lo que entra por HTTP
class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str       # NO existe en el Model
    age: int
    # is_admin NO está acá: el cliente no puede setearlo
```

---

## Flujo completo

```
Cliente HTTP
    │  JSON crudo
    ▼
[Router/FastAPI] ── valida con Schema (Pydantic) ──► CreateUserDTO
    │
    ▼
[Service] ── lógica de negocio ──► usa el DTO
    │
    ▼
[Repository] ── traduce DTO ──► Model (SQLAlchemy)
    │
    ▼
Base de datos
    │
    ▲
[Repository] devuelve Model
    │
    ▼
[Service] ── mapea Model ──► UserResponseDTO
    │
    ▼
[Router] ── responde JSON ──► Cliente
```

**Regla clave**: el `Model` **no debe escaparse** del repositorio/service. Lo que sale al cliente siempre es un DTO.

---

## Estructura por capas (horizontal)

```
proyecto/
├── src/
│   ├── db/
│   │   ├── connection.py          # engine, SessionLocal, Base
│   │   ├── models/                # definiciones de tablas (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   ├── user_model.py
│   │   │   ├── product_model.py
│   │   │   └── order_model.py
│   │   ├── migrations/            # Alembic
│   │   │   └── versions/
│   │   └── seeders/
│   │       └── users_seeder.py
│   │
│   ├── schemas/                   # validación de entrada (Pydantic)
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   └── auth_schema.py
│   │
│   ├── dtos/                      # contratos entre capas (Pydantic)
│   │   ├── __init__.py
│   │   ├── user_dto.py
│   │   ├── product_dto.py
│   │   └── auth_dto.py
│   │
│   ├── mappers/                   # Model ⇄ DTO
│   │   ├── __init__.py
│   │   ├── user_mapper.py
│   │   └── product_mapper.py
│   │
│   ├── repositories/              # acceso a datos (queries)
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   └── product_repository.py
│   │
│   ├── services/                  # lógica de negocio
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   └── auth_service.py
│   │
│   ├── routers/                   # endpoints (FastAPI APIRouter)
│   │   ├── __init__.py
│   │   ├── user_router.py
│   │   ├── product_router.py
│   │   └── auth_router.py
│   │
│   ├── middlewares/
│   │   ├── __init__.py
│   │   ├── auth_middleware.py     # JWT / sesión
│   │   ├── error_middleware.py    # captura excepciones
│   │   └── logger_middleware.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── env.py                 # carga .env y valida con Pydantic Settings
│   │   └── constants.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── hash.py
│   │   ├── jwt.py
│   │   └── errors.py              # AppError, NotFoundError, etc.
│   │
│   ├── app.py                     # crea la app FastAPI, registra middlewares y routers
│   └── main.py                    # punto de entrada (uvicorn)
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── pyproject.toml
```

---

## Cómo se relacionan las carpetas (flujo de un request)

```
HTTP request
   │
   ▼
routers/user_router.py
   │ FastAPI valida automáticamente con:
   ▼
schemas/user_schema.py  (Pydantic BaseModel)
   │
   ▼
service llamado desde el router
   │ recibe el body validado como ──► dtos/user_dto.py
   ▼
services/user_service.py            (lógica de negocio)
   │
   ▼
repositories/user_repository.py     (queries)
   │
   ▼
db/models/user_model.py             (SQLAlchemy)
   │
   ▼
Base de datos
```

A la vuelta, el `service` usa `mappers/user_mapper.py` para convertir el `Model` en un `UserResponseDTO` antes de devolverlo al `router`.

---

## Ejemplo mínimo conectando todo (FastAPI + SQLAlchemy + Pydantic)

### `schemas/user_schema.py`
```python
from pydantic import BaseModel, EmailStr, Field

class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(ge=18)
```

### `dtos/user_dto.py`
```python
from pydantic import BaseModel
from datetime import datetime

class CreateUserDTO(BaseModel):
    email: str
    password: str
    age: int

class UserResponseDTO(BaseModel):
    id: int
    email: str
    age: int
    created_at: datetime

    model_config = {"from_attributes": True}
```

### `db/connection.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config.env import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### `db/models/user_model.py`
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from db.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
```

### `mappers/user_mapper.py`
```python
from db.models.user_model import User
from dtos.user_dto import UserResponseDTO

def to_user_response(user: User) -> UserResponseDTO:
    return UserResponseDTO.model_validate(user)
```

### `repositories/user_repository.py`
```python
from sqlalchemy.orm import Session
from db.models.user_model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, password_hash: str, age: int) -> User:
        user = User(email=email, password_hash=password_hash, age=age)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def find_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
```

### `services/user_service.py`
```python
from sqlalchemy.orm import Session
from dtos.user_dto import CreateUserDTO, UserResponseDTO
from repositories.user_repository import UserRepository
from mappers.user_mapper import to_user_response
from utils.hash import hash_password

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create(self, dto: CreateUserDTO) -> UserResponseDTO:
        password_hash = hash_password(dto.password)
        user = self.repo.create(
            email=dto.email,
            password_hash=password_hash,
            age=dto.age,
        )
        return to_user_response(user)
```

### `routers/user_router.py`
```python
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.connection import get_db
from schemas.user_schema import CreateUserSchema
from dtos.user_dto import CreateUserDTO, UserResponseDTO
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED)
def create_user(payload: CreateUserSchema, db: Session = Depends(get_db)):
    dto = CreateUserDTO(**payload.model_dump())
    return UserService(db).create(dto)
```

### `middlewares/error_middleware.py`
```python
from fastapi import Request
from fastapi.responses import JSONResponse
from utils.errors import AppError

async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message},
    )
```

### `app.py`
```python
from fastapi import FastAPI
from routers import user_router, auth_router
from middlewares.error_middleware import app_error_handler
from utils.errors import AppError

app = FastAPI(title="Mi API")

app.add_exception_handler(AppError, app_error_handler)

app.include_router(user_router.router, prefix="/api")
app.include_router(auth_router.router, prefix="/api")
```

### `main.py`
```python
import uvicorn
from config.env import settings

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=settings.PORT, reload=True)
```

### `config/env.py`
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    PORT: int = 8000
    JWT_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()
```

---

## Reglas que mantienen sana esta estructura

1. **`routers` no tocan la BD.** Solo llaman al `service`.
2. **`services` no tocan `Request`/`Response`.** Reciben DTOs y devuelven DTOs.
3. **`repositories` no tienen lógica de negocio.** Solo queries.
4. **`models` no salen del `repository`/`service`.** Al cliente siempre va un DTO.
5. **`schemas` solo se usan en los routers** para validar entrada, no dentro del service.
6. **`routers` son delgados**: ruta + dependencias + llamada al service.

---

## Por qué separar las tres capas

| Problema si NO separás | Consecuencia |
|---|---|
| Devolvés el Model al cliente | Filtrás `password_hash`, `is_admin`, etc. |
| Validás dentro del service | Lógica acoplada a HTTP, difícil de testear |
| Usás el Schema como tipo interno | Cualquier cambio de API rompe el dominio |
| Pasás el Model entre servicios | Acoplás la lógica al ORM elegido |

La separación cuesta un poco más de boilerplate, pero te da: **seguridad** (no fugás campos), **testeabilidad** (services puros) y **flexibilidad** (cambiar ORM o framework HTTP sin tocar el dominio).

---

## Schema vs DTO en Pydantic: ¿cuándo fusionarlos?

Como ambos se escriben con `BaseModel`, en proyectos chicos es común usar una sola clase para los dos roles.

| Caso | Recomendación |
|---|---|
| API chica, contrato HTTP = contrato interno | Una sola clase Pydantic (schema = DTO) |
| El service necesita campos derivados (ej. `password_hash` en vez de `password`) | Separar: Schema valida entrada, DTO transporta lo que el service necesita |
| Querés versionar la API (`v1`, `v2`) sin tocar el dominio | Separar siempre |
| Output con campos calculados o agregados | DTO de respuesta separado del Model |

---

## Cuándo conviene esta estructura vs. modular

| Por capas (esta) | Por módulos |
|---|---|
| Proyecto chico/mediano | Proyecto grande |
| Pocos dominios | Muchos dominios independientes |
| Equipo chico | Varios equipos en paralelo |
| Fácil de aprender | Mejor aislamiento |
