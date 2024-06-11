from core.database import connectToDatabase
import mysql.connector
from typing import List, Optional
from models.HorariosModel import *

def todosHorarios() -> List[Horario]:
    connection = connectToDatabase()

    horarios = []

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT idHorario, Fecha, Hora, idMedico FROM Horarios"
        cursor.execute(query)
        for row in cursor.fetchall():
            horario = Horario(**row)
            horarios.append(horario)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return horarios

def buscarHorasPorEspecialidadYFecha(Medico, Fecha)->List[HorarioInfo]:
    connection = connectToDatabase()

    horarios = []

    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT h.idHorario, h.Hora, h.Fecha, pe.Nombre, pe.Apellido FROM Horarios AS h INNER JOIN Personas AS pe ON pe.idPersona = h.idMedico WHERE h.Fecha = %s AND h.idMedico = %s"
        cursor.execute(query,(Fecha, Medico))
        for row in cursor.fetchall():
            horario = HorarioInfo(**row)
            horarios.append(horario)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return horarios