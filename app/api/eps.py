from fastapi import APIRouter
from cruds.crudEps import *

router = APIRouter(tags = ["EPS"])

@router.get("/eps")
def getAllEps():
    eps = todasEps()
    return {"eps": eps}

@router.get("/eps/{idEps}")
def getGeneroById(idEps: int):
    eps = buscarEpsPorId(idEps)
    return {"eps": eps}