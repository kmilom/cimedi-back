from pydantic import BaseModel

class Paciente(BaseModel):
    idPaciente: int
    idEPS: int