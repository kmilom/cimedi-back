from fastapi import APIRouter
from cruds.crudPersona import *

router = APIRouter(tags=["Personas"])

@router.get("/personas")
def readAllPersonas():
    personas = TodasPersonas()
    return {"personas": personas}

@router.get("/personas/{idPersona}")
def ReadPeronaById(idPersona: int):
    persona = buscarPersonaPorId(idPersona)
    return {"persona": persona}

@router.post("/crear-persona")
def createPersona(persona: PersonaCreate):
    idPersona = crearPersona(persona)
    if(idPersona != 0):
        return {"idPersona": idPersona}
    else:
        return {"Message": "Error al crear la persona!"}
    
@router.put("/editar-persona/{idPersona}")
def updatePersona(idPersona: int, persona:Persona):
    persona.idPersona = idPersona
    if editarPersona(persona):
        return {"Message": "Persona editada correctamente!"}
    else:
        return {"Message": "No se pudo editar la persona!"}
    
@router.delete("/eliminar-persona/{idPersona}")
def updatePersona(idPersona: int):
    if eliminarPersona(idPersona):
        return {"Message": "Persona eliminada correctamente!"}
    else:
        return {"Message": "No se pudo eliminar la persona!"}