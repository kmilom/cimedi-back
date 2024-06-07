from pydantic import BaseModel
from datetime import date

class Paciente(BaseModel):
    idPaciente: int
    idEPS: int

class PacienteInfo(BaseModel):
    idPaciente: int
    Nombre: str
    Apellido: str
    Correo: str
    FechaNacimiento: date
    Tipo: str
    Documento: int
    Genero: str
    EPS: str