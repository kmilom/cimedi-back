from fastapi import APIRouter
from cruds.crudHorario import *

router = APIRouter(tags=["Horarios"])

@router.get("/horarios")
def getAllHorarios():
    horarios = todosHorarios()
    return { "horarios": horarios}

@router.get("/horarios-por-fecha-medico")
def getHorariosByFecha(idMedico: str, Fecha: str):
    horarios = buscarHorasPorEspecialidadYFecha(idMedico, Fecha)
    return { "horarios": horarios} 