from fastapi import APIRouter
from cruds.crudUsuario import *

router = APIRouter(tags=["Usuarios"])

@router.get("/usuarios")
def readAllUsuarios():
    usuarios = todosUsuarios()
    return {"Usuarios": usuarios}

@router.get("/usuarios/{idUsuario}")
def readUsuarioById(idUsuario: int):
    usuario = buscarUsuarioPorId(idUsuario)
    return {"Usuario": usuario}

@router.post("/crear-usuario")
def createUsuario(usuario: Usuario):
    if(crearUsuario(usuario)):
        return {"Message": "Usuario creado exitosamente!"}
    else:
        return {"Message": "Error al crear el usuario!"}


@router.put("/editar-usuario/{idUsuario}")
def updateUsuario(idUsuario: int, usuario: Usuario):
    usuario.idUsuario = idUsuario
    if editarUsuario(usuario):
        return {"Message": "Usuario editado correctamente!"}
    else:
        return {"Message": "No se pudo editar el usuario!"}
    
@router.delete("/eliminar-usuario/{idUsuario}")
def deleteUsuario(idUsuario: int):
    if(eliminarUsuario(idUsuario)):
        return {"Message": "Usuario eliminado correctamente!"}
    else:
        return {"Message": "Error al eliminar el usuario"}