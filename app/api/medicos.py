from fastapi import APIRouter
from cruds.crudMedico import *

router = APIRouter(tags=["Medicos"])

@router.get("/medicos")
def getAllMedicos():
    medicos = todoMedicos()
    return { "Medicos": medicos }

@router.get("/info-medico/{idMedico}")
def getInfoMedicoByIp(idMedico: int):
    medico = obtenerInfoMedicoPorId(idMedico)
    return { "Medico": medico }