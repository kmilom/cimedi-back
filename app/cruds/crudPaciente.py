from core.database import connectToDatabase
import mysql.connector
from typing import List, Optional
from models.pacienteModel import Paciente

def todosPacientes() -> List[Paciente]:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor(dictionary=True)

        pacientes = []

        query = "SELECT idPaciente, idEPS FROM Pacientes"
        cursor.execute(query)

        for row in cursor.fetchall():
            paciente = Paciente(**row)
            pacientes.append(paciente)
        
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return pacientes

def buscarPacientePorId(idPaciente: int)-> Optional[Paciente]:
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        paciente = None

        query = "SELECT idPaciente, idEPS FROM Pacientes WHERE idPaciente = %s"
        cursor.execute(query,(idPaciente,))

        row = cursor.fetchone()
        if row:
            paciente = row
    except mysql.connector.Error as e:
        # Manejar error de base de datos
        print(f"Error al obtener lista de pacientes: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
    return paciente

def crearPaciente(paciente: Paciente):
    connection = connectToDatabase()

    try:
        cursor = connection.cursor()

        query = "INSERT INTO Pacientes (idPaciente, idEPS) VALUES (%s, %s)"
        cursor.execute(query, (paciente.idPaciente, paciente.idEPS))
        connection.commit()
        return True
    except Exception as e:
        print(f"Error al crear paciente: {e}")
        return False
    finally:
        connection.close()