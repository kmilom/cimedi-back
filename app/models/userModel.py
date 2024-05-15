from pydantic import BaseModel

class Usuario(BaseModel):
    idUsuario: int
    User: str
    Password: str
    idRol: int