from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    idUsuario: Optional[int] = None
    User: str
    Password: str
    idRol: int