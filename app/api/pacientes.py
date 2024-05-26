from fastapi import APIRouter
from cruds.crudPaciente import *

router = APIRouter(tags=["Pacientes"])

@router.get("/pacientes")
def getAllPacientes():
    pacientes = todosPacientes()
    return { "pacientes": pacientes }

@router.get("/pacientes/{idPaciente}")
def getPacienteById(idPaciente: int):
    paciente = buscarPacientePorId(idPaciente)
    return { "paciente": paciente }

@router.post("/crear-paciente")
def createPaciente(paciente: Paciente):
    if(crearPaciente(paciente)):
        return {"Message": "Paciente creado exitosamente!"}
    else:
        return {"Message": "Error al crear el paciente!"}