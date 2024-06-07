from pydantic import BaseModel

class Usuario(BaseModel):
    idUsuario: int
    User: str
    Password: str
    idRol: int

class UsuarioInfo(BaseModel):
    idUsuario: int
    User: str
    Password: str
    Rol: str