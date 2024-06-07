from core.database import connectToDatabase
import mysql.connector
from typing import List, Optional
from models.MedicoModel import *

def todosMedicos()-> List[Medico]:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor(dictionary=True)

        medicos = []
        query = "SELECT idMedico, idEspecialidad FROM Medicos"
        cursor.execute(query)

        for row in cursor.fetchall():
            medico = Medico(**row)
            medicos.append(medico)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return medicos

def todosMedicosInfo()-> List[MedicoInfo]:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor(dictionary=True)

        medicos = []
        query = "SELECT m.idMedico, p.Nombre, p.Apellido, e.Especialidad FROM Medicos AS m INNER JOIN Personas AS p ON m.idMedico = p.idPersona INNER JOIN Especialidades AS e ON m.IdEspecialidad = e.IdEspecialidad"
        cursor.execute(query)

        for row in cursor.fetchall():
            medico = MedicoInfo(**row)
            medicos.append(medico)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return medicos

def obtenerInfoMedicoPorId(idMedico: int)-> Optional[Medico]:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        medico = None

        query = "SELECT m.idMedico, p.Nombre, p.Apellido, e.Especialidad FROM Medicos AS m INNER JOIN Personas AS p ON m.idMedico = p.idPersona INNER JOIN Especialidades as e ON m.IdEspecialidad = e.IdEspecialidad WHERE m.idMedico = %s"
        cursor.execute(query,(idMedico,))

        row = cursor.fetchone()
        if row:
            medico = row
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return medico

def medicosPorEspecialidad(idEspecialidad: int) -> List[MedicoInfo]: 
    connection = connectToDatabase()

    try:
        cursor = connection.cursor(dictionary=True)

        medicos = []

        query = "SELECT m.idMedico, p.Nombre, p.Apellido, e.Especialidad FROM Medicos AS m INNER JOIN Personas AS p ON m.idMedico = p.idPersona INNER JOIN Especialidades AS e ON m.idEspecialidad = e.idEspecialidad WHERE m.idEspecialidad = %s"
        cursor.execute(query,(idEspecialidad,))

        for row in cursor.fetchall():
            medico = MedicoInfo(**row)
            medicos.append(medico)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return medicos