from fastapi import APIRouter
from cruds.crudMedico import *

router = APIRouter(tags=["Medicos"])

@router.get("/medicos")
def getAllMedicos():
    medicos = todosMedicos()
    return { "Medicos": medicos }

@router.get("/medicos-info")
def getAllMedicos():
    medicos = todosMedicosInfo()
    return { "Medicos": medicos }

@router.get("/info-medico/{idMedico}")
def getInfoMedicoByIp(idMedico: int):
    medico = obtenerInfoMedicoPorId(idMedico)
    return { "Medico": medico }

@router.get("/medicos-por-especialidad/{idEspecialidad}")
def getMedicoByEspecialidad(idEspecialidad: int):
    medicos = medicosPorEspecialidad(idEspecialidad)
    return { "Medico": medicos }