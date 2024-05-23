from fastapi import APIRouter
from cruds.crudTipoDocumento import *

router = APIRouter(tags=["Tipos de Documento"])

@router.get("/tipos-de-documento")
def getAllTiposDocumentos():
    tiposDocumentos = todosTipoDocumentos()
    return tiposDocumentos

@router.get("/tipos-de-documento/{idTipoDocumento}")
def getTipoDocumentoById(idTipoDocumento: int):
    tipoDocumento = buscarTipoDocumentoPorId(idTipoDocumento)
    return tipoDocumento