import mysql.connector
from typing import List, Optional
from core.database import connectToDatabase
from models.tipoDocumentoModel import TipoDocumento

def todosTipoDocumentos() -> List[TipoDocumento]:
    connection = connectToDatabase()
    
    tipoDocumentos = []

    try:
        cursor = connection.cursor(dictionary = True)

        query = "SELECT idTipoDocumento, Tipo FROM TiposDocumentos"
        cursor.execute(query)

        for row in cursor.fetchall():
            tipoDocumento = TipoDocumento(**row)
            tipoDocumentos.append(tipoDocumento)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de generos: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    
    return tipoDocumentos

def buscarTipoDocumentoPorId(idTipoDocumento: int) -> Optional[TipoDocumento]:
    connection = connectToDatabase()

    tipoDocumento = None

    try:
        cursor = connection.cursor(dictionary = True)

        query = "SELECT idTipoDocumento, Tipo FROM TiposDocumentos WHERE idTipoDocumento = %s"
        cursor.execute(query, (idTipoDocumento,))
        row = cursor.fetchone()
        if row:
            tipoDocumento = TipoDocumento(**row)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de generos: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

    return tipoDocumento