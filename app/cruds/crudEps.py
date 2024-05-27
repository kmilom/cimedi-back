from core.database import connectToDatabase
import mysql.connector
from typing import List, Optional
from models.EpsModel import Eps

def todasEps() -> List[Eps]:
    connection = connectToDatabase()

    eps_list = []

    try:
        cursor = connection.cursor(dictionary=True)
        query = ("SELECT idEPS, Nombre FROM eps")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            eps = Eps(**row)
            eps_list.append(eps)
        
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de EPS: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return eps_list

def buscarEpsPorId(idEPS: int) -> Optional[Eps]:
    connection = connectToDatabase()

    result = None

    try:
        cursor = connection.cursor(dictionary = True)

        query = "SELECT idEPS, Nombre FROM EPS WHERE idEPS = %s"
        cursor.execute(query, (idEPS,))
        row = cursor.fetchone()
        if row:
            result = Eps(**row)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de generos: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

    return result