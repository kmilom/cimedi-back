from core.database import connectToDatabase
import mysql.connector
from typing import List, Optional
from models.CitaModel import *

def TodasCitas() -> List[Cita]:
    connection = connectToDatabase()

    citas = []

    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT idCitas, ListaEspera, idEspecialidad, idHorario, idEstadoCita, idPaciente, idMedico FROM Citas"
        cursor.execute(query)
        for row in cursor.fetchall():
            cita = Cita(**row)
            citas.append(cita)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return citas

def crearCita(cita: CitaCreate):
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        query = "INSERT INTO Citas (ListaEspera, idEspecialidad, idHorario, idEstadoCita, idPaciente, idMedico) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (cita.ListaEspera, cita.idEspecialidad, cita.idHorario, cita.idEstadoCita, cita.idPaciente, cita.idMedico))
        idPersona = cursor.lastrowid
        connection.commit()
        return idPersona
    except Exception as e:
        print(f"Error al crear persona: {e}")
        return False
    finally:
        connection.close()