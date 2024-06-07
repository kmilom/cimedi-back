from fastapi import APIRouter
from cruds.crudEspecialidad import *

router = APIRouter(tags=["Especialidades"])

@router.get("/especialidades")
def getAllEspecialidades():
    especialidades = todasEspecialidades()
    return { "especialidades": especialidades}