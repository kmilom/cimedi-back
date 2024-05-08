from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    idUsuario: int
    User: str
    Password: str
    idRol: int