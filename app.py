from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Crear el modelo Usuario
class Usuario(BaseModel):
    nombre: str
    telefono: str
    email: str
    latitude: float
    longitude: float
    image: str

# Definir el modelo de respuesta
class UsuarioResponse(BaseModel):
    status: str
    message: str
    usuarios: List[Usuario]


# Crear la aplicación FastAPI
app = FastAPI()

# Lista de usuarios simulados (en un caso real se obtendría de una base de datos)
usuarios_db = [
    Usuario(
        nombre="Juan Pérez",
        telefono="123456789",
        email="juanperez@email.com",
        latitude=19.4326,
        longitude=-99.1332,
        image="https://cdn-icons-png.flaticon.com/512/219/219970.png"
    ),
    Usuario(
        nombre="María López",
        telefono="987654321",
        email="marialopez@email.com",
        latitude=40.7128,
        longitude=-74.0060,
        image="https://cdn-icons-png.freepik.com/512/219/219966.png"
    )
]

# Crear el controlador GET para obtener la lista de usuarios
@app.get("/usuarios", response_model=UsuarioResponse)
def get_usuarios():
    response = UsuarioResponse(
        status="success",
        message="Usuarios obtenidos correctamente",
        usuarios=usuarios_db
    )
    return response

# Configuración para ejecutar la API
# Guarda este archivo como app.py y ejecuta con el siguiente comando:
# uvicorn app:app --reload
