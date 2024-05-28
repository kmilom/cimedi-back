from pydantic import BaseModel

class Medico(BaseModel):
    idMedico: int
    idEspecialidad: int

class MedicoInfo(BaseModel):
    idMedico: int
    Nombre: str
    Apellido: str
    Especialidad: str