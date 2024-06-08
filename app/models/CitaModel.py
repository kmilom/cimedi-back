from pydantic import BaseModel
from datetime import date

class Cita(BaseModel):
    idCitas: int
    ListaEspera: bool
    idEspecialidad: int
    idHorario: int
    idEstadoCita: int 
    idPaciente: int 
    idMedico: int

class CitaInfo(BaseModel):
    idCitas: int
    ListaEspera: bool
    Especialidad: str
    Fecha: date
    Hora: str
    EstadoCita: str
    Nombre: str
    Apellido: str
    Nombre: str
    Apellido: str

class CitaCreate(BaseModel):
    ListaEspera: bool
    idEspecialidad: int
    idHorario: int
    idEstadoCita: int 
    idPaciente: int 
    idMedico: int