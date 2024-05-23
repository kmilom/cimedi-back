from pydantic import BaseModel
from datetime import date

class Persona(BaseModel):
    idPersona: int
    Nombre: str
    Apellido: str
    Correo: str
    FechaNacimiento: date
    idTipoDocumento: int
    Documento: int
    idGenero: int

class PersonaCreate(BaseModel):
    Nombre: str
    Apellido: str
    Correo: str
    FechaNacimiento: date
    idTipoDocumento: int
    Documento: int
    idGenero: int