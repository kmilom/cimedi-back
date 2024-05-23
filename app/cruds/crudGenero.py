import mysql.connector
from typing import List, Optional
from core.database import connectToDatabase
from models.generoModel import Genero

def todosGeneros() -> List[Genero]:
    connection = connectToDatabase()
    
    generos = []

    try:
        cursor = connection.cursor(dictionary = True)

        query = "SELECT idGenero, Genero FROM Generos"
        cursor.execute(query)

        for row in cursor.fetchall():
            genero = Genero(**row)
            generos.append(genero)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de generos: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    
    return generos

def buscarGeneroPorId(idGenero: int) -> Optional[Genero]:
    connection = connectToDatabase()

    genero = None

    try:
        cursor = connection.cursor(dictionary = True)

        query = "SELECT idGenero, Genero FROM Generos WHERE idGenero = %s"
        cursor.execute(query, (idGenero,))
        row = cursor.fetchone()
        if row:
            genero = Genero(**row)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de generos: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

    return genero