from typing import List, Optional
import mysql.connector
from core.database import connectToDatabase
from models.PersonaModel import Persona, PersonaCreate

def TodasPersonas() -> List[Persona]:
    connection = connectToDatabase()

    personas = []

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT idPersona, Nombre, Apellido, Correo, FechaNacimiento, idTipoDocumento, Documento, idGenero FROM Personas"
        cursor.execute(query)

        for row in cursor.fetchall():
            persona = Persona(**row)
            personas.append(persona)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de personas: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

    return personas

def buscarPersonaPorId(idPersona: int)-> Optional[Persona]:
    connection = connectToDatabase()

    persona = None

    try:
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT idPersona, Nombre, Apellido, Correo, FechaNacimiento, idTipoDocumento, Documento, idGenero FROM Personas WHERE idPersona = %s"

        cursor.execute(query,(idPersona,))
        row = cursor.fetchone()
        if row:
            persona = Persona(**row)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener persona: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return persona

def crearPersona(persona: PersonaCreate):
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        query = "INSERT INTO Personas (Nombre, Apellido, Correo, FechaNacimiento, idTipoDocumento, Documento, idGenero) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (persona.Nombre, persona.Apellido, persona.Correo, persona.FechaNacimiento, persona.idTipoDocumento, persona.Documento, persona.idGenero))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error al crear persona: {e}")
        return False
    finally:
        connection.close()

def editarPersona(persona: Persona) -> bool:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        query = "UPDATE Personas SET idPersona = %s, Nombre = %s, Apellido = %s, Correo = %s, FechaNacimiento = %s, idTipoDocumento = %s, Documento = %s, idGenero = %s WHERE idPersona = %s"
        cursor.execute(query, (persona.idPersona, persona.Nombre, persona.Apellido, persona.Correo, persona.FechaNacimiento, persona.idTipoDocumento, persona.Documento, persona.idGenero, persona.idPersona))
        connection.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Error al editar persona: {e}")
        return False
    finally:
        connection.close()

def eliminarPersona(idPersona: int) -> bool:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        query = "DELETE FROM Personas WHERE idPersona = %s"
        cursor.execute(query, (idPersona,))
        connection.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Error al eliminar persona {e}")
        return False
    finally:
        connection.close()