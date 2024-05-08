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
