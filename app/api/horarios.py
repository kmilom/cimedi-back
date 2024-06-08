from fastapi import APIRouter
from cruds.crudHorario import *

router = APIRouter(tags=["Horarios"])

@router.get("/horarios")
def getAllHorarios():
    horarios = todosHorarios()
    return { "horarios": horarios}

@router.get("/horarios/{Fecha}")
def getHorariosByFecha(Fecha: str):
    horarios = buscarHorasPorFecha(Fecha)
    return { "horarios": horarios}