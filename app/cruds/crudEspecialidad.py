from core.database import connectToDatabase
import mysql.connector
from typing import List, Optional
from models.especialidadModel import Especialidad

def todasEspecialidades() -> List[Especialidad]:
    connection = connectToDatabase()

    especialidades = []

    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT idEspecialidad, Especialidad FROM Especialidades"
        cursor.execute(query)
        for row in cursor.fetchall():
            especialidad = Especialidad(**row)
            especialidades.append(especialidad)
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return especialidades