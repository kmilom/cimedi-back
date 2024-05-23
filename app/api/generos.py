from fastapi import APIRouter
from cruds.crudGenero import *

router = APIRouter(tags = ["Generos"])

@router.get("/generos")
def getAllGeneros():
    generos = todosGeneros()
    return {"generos": generos}

@router.get("/generos/{idGenero}")
def getGeneroById(idGenero: int):
    genero = buscarGeneroPorId(idGenero)
    return {"genero": genero}