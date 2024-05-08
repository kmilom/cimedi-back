from typing import Union
from fastapi import FastAPI
from core.database import connectToDatabase
import mysql.connector
from cruds.crudUsuario import *
from cruds.crudEps import *

app = FastAPI()
connection = connectToDatabase()
cursor = connection.cursor()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/usuarios")
def readAllUsuarios():
    usuarios = getAllUsuarios()
    return {"Usuarios": usuarios}

@app.get("/usuarios/{idUsuario}")
def readUsuario(idUsuario: int):
    usuario = getUsuario(idUsuario)
    return {"Usuario": usuario}

@app.get("/eps")
def readEps():
    
    try:
        results = getAllEps()
        return {"EPS": results}
    except mysql.connector.Error as e:
        print(e)
        message = f"Error al conectar: {e}"
        statusCode = 500
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
    return {"message": message}, statusCode


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}