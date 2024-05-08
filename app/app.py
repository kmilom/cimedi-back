from fastapi import FastAPI
from cruds.crudUsuario import *
from cruds.crudEps import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/usuarios")
def readAllUsuarios():
    usuarios = getAllUsuarios()
    return {"Usuarios": usuarios}

@app.get("/usuarios/{idUsuario}")
def readUsuarioById(idUsuario: int):
    usuario = getUsuarioById(idUsuario)
    return {"Usuario": usuario}

@app.post("/crear-usuario")
def createUsuario(usuario: Usuario):
    if(crearUsuario(usuario)):
        return {"Message": "Usuario creado exitosamente!"}
    else:
        return {"Message": "Error al crear el usuario!"}


@app.put("/editar-usuario/{idUsuario}")
def updateUsuario(idUsuario: int, usuario: Usuario):
    usuario.idUsuario = idUsuario
    print(usuario)
    if editarUsuario(usuario):
        return {"Message": "Usuario editado correctamente!"}
    else:
        return {"Message": "No se pudo editar el usuario!"}
    
@app.delete("/eliminar-usuario/{idUsuario}")
def deleteUsuario(idUsuario: int):
    if(eliminarUsuario(idUsuario)):
        return {"Message": "Usuario eliminado correctamente!"}
    else:
        return {"Message": "Error al eliminar el usuario"}