from fastapi import APIRouter
from cruds.crudCitas import *

router = APIRouter(tags=["Citas"])

@router.get("/citas")
def getAllCitas():
    citas = TodasCitas()
    return { "Citas": citas}

@router.post("/crear-cita")
def createCita(cita: CitaCreate):
    if(crearCita(cita)):
        return { "Message": "Creada"}
    else:
        return { "Message": "Error al crearla"} 