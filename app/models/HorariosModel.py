from pydantic import BaseModel
from datetime import date

class Horario(BaseModel):
    idHorario: int
    Fecha: date
    Hora: str
    idMedico: int

class HorarioInfo(BaseModel):
    idHorario: int
    Fecha: date
    Hora: str
    Nombre: str
    Apellido: str

